# DisputeDesk v1 (trial) — build specification

## 1. Scope

One immutable Solidity contract, **Ethereum mainnet**, denominated
in **IMD**. No proxy, no upgradeability, no delegatecall: post-trial
changes ship as a new deployment; the economics dials below cover
everything meant to move. Trial/beta status is stated in the
contract's metadata string and README; verdicts bind from day one.

## 2. Deploy parameters (constructor)

| param | value at deploy |
|---|---|
| IMD token | `0xd34a99bc0f67ae1bbd63c660e6d0b0dd03e263b7` |
| Intake | `0xa43e6f75ee006411f79ac1c84120606c2330de82` |
| owner (newsroom wallet) | `0xbe80e5979313cf8aff2b8e54e615fe3ecd8358f5` |
| bond | 1 IMD (1e18) |
| bountyMultiplier | 1x bond |
| oracleFee | 0.5 IMD (the network's oracle price; settable, below) |
| rubricHash | sha256 of the rubric text in force (bytes32) |

CONSTRUCTOR ARGS ARE STATIC ONLY (network rule for evm_contracts
launches, confirmed against live docs 2026-11-11: address, uint,
bool, bytes32 — no strings). The two URI strings are therefore NOT
constructor params: the owner sets them right after deploy, before
the pool is seeded — `setRubric(rubricHash, rubricURI)` (same hash,
adds the URI) and `setRecordURI(recordURI)`. Until both are set the
contract is paused for new filings (deploy with paused = true; the
owner unpauses after the two setters and the pool seed).

## 3. Terms lock at filing

Every challenge freezes ITS OWN bond, bounty, oracleFee and
rubricHash at the moment of filing. Dial changes NEVER touch an
open challenge; they apply to future filings only. This is the
contract-level form of "trial terms change only with public
notice, never mid-dispute."

## 4. State

`Challenge { challenger, bondPaid, bountyDue, editionHash,
claimHash, evidenceURI, evidenceHash, rubricHash, status,
oracleRef, filedAt }`
with status in `Open | Upheld | Rejected | Failed`. Plus:
- one-active-per-claim: mapping claimHash → active challenge id;
- cooldown: mapping claimHash → timestamp before which a rejected
  claim cannot be re-filed (COOLDOWN_SECONDS = 7 days — DECIDED,
  her confirmation 2026-11-11);
- max 3 Open challenges per challenger address;
- pool accounting: poolBalance and reservedBounties, tracked
  separately from escrowed bonds at all times. A filing reserves
  the pool's FULL potential outflow at its locked terms, bounty +
  oracleFee (1.5 at trial numbers) — not bounty alone, which
  would let the pool accept a challenge it cannot pay. (Fixed
  2026-11-11 during the job-body rewrite; §5's uphold math always
  drew 1.5.)

## 5. Money flow — escrow until verdict, never before

The bond is pulled by `transferFrom` at filing and ESCROWED. The
only amount spent before the verdict is the oracle fee, paid to
Intake when the request opens. Distribution happens at settlement
only:

- **Filing**: 1.0 in → 0.5 to Intake as the oracle fee → 0.5
  remainder held in escrow. Bounty + fee (1.5) reserved in the
  pool (the uphold's full pool draw).
- **REJECTED**: escrowed 0.5 → newsroom wallet. Reservation
  released. Cooldown starts on the claimHash.
- **UPHELD**: challenger receives 2.0 — the 0.5 escrow remainder
  plus 1.5 from the pool (refund made whole + 1x bounty). Emit
  `Correction(editionHash, claimHash, verdictRef)`. Pool cost per
  uphold: 1.5; desk cost all-in: 2.0. (Corrects the earlier 2.0/2.5
  figures in DISPUTES-SPEC, which assumed the remainder was
  distributed at filing; escrow-until-verdict is the required
  design and the cheaper one.)
- **FAILED / REFUSED** (panel failure, via the failure callback):
  escrowed 0.5 returned to the challenger (bond minus the spent
  fee). Reservation released. NO cooldown: the claim may be
  re-filed at once.

## 6. Functions

- `challenge(bytes32 editionHash, bytes32 claimHash, string
  evidenceURI, bytes32 evidenceHash)` — evidenceHash is OPTIONAL
  (her call 2026-11-11): zero means the evidence is unpinned; a
  nonzero value is the sha256 of the material at evidenceURI,
  freezing the evidence at filing the way the terms freeze.
  Reverts when: paused; an Open challenge exists on
  claimHash; claimHash is in cooldown; caller has 3 Open; or
  poolBalance − reservedBounties < bounty + oracleFee (the solvency
  rule: never accept a challenge the pool cannot pay in full). On
  success: escrow,
  reserve, open the oracle request via Intake's on-chain
  `request()`/`requestWithFailure()` path with the callback set to
  this contract, emit `ChallengeFiled`.
- Oracle callbacks — callable ONLY by Intake; match on oracleRef;
  settle exactly one Open challenge exactly once.
- `fundPool(uint256 amount)` — anyone, any time. The pool's only
  intake. One-way valve: NO function withdraws from the pool;
  nothing leaves except bounty payments at settlement.
- `setBond(uint256)` / `setBountyMultiplier(uint256)` /
  `setOracleFee(uint256)` / `setRubric(bytes32 hash, string uri)` /
  `setRecordURI(string uri)` / `setIntake(address)` — owner only,
  future filings only, each emits a public event (the disclosure
  trail). setIntake restored 2026-11-11 on the network's own
  documented advice ("keep the intake address settable in your
  contract" — versions land at new addresses). Each challenge
  LOCKS the intake address it was filed through; its callbacks
  validate against that address, so an intake change never
  touches an open challenge's settlement path.
- `setPaused(bool)` — owner only; blocks NEW filings only. Open
  challenges always settle.
- There is NO: verdict override, escrow touch, pool withdrawal,
  challenge cancellation, or owner path to any challenger's funds.

## 7. The oracle request

Action: the network's oracle question, opened on-chain by the
contract itself (the trustless trick — no bot, no human relay).
The body carries: the question and rubric (by rubricURI +
rubricHash), editionHash, claimHash, evidenceURI, evidenceHash,
and the edition's public record URL. When evidenceHash is nonzero
the body instructs the panel to verify the fetched material's
sha256 against it and, on a mismatch, to treat the evidence as
absent (the burden rule then decides). This instruction lives in
the oracle body, not the rubric: the rubric stays at v0.1. Panel: **size 5, quorum 3** (DECIDED, her
confirmation 2026-11-11 — the court sits larger than the
newsroom's panels).
Answer form: UPHELD/REJECTED plus the short reason the rubric
requires. Contract builders work offline (network rule,
confirmed 2026-11-11): the exact oracle-body template and the
Intake interface are PASTED into the job objective from the live
docs at job-assembly time; the builder conforms to the pasted
text and fetches nothing.

## 8. Events — the site renders from these, permanently

`ChallengeFiled`, `ChallengeSettled(status)`, `Correction(
editionHash, claimHash, verdictRef)`, `PoolFunded`, `BondChanged`,
`FeeChanged`, `BountyChanged`, `RubricChanged`, `Paused`. The
/disputes page and the corrections ledger read ONLY the event log
via public RPC; no server, no database.

## 9. Security requirements (acceptance-gating)

Checks-effects-interactions everywhere; reentrancy guard on
filing and settlement; ERC-20 return values checked (safe
transfer); callbacks validate caller == Intake AND a known, Open
oracleRef; no unbounded loops; no selfdestruct; solidity ^0.8
checked arithmetic; every state change emits an event. Foundry
tests MUST cover, at minimum: the three settlement paths; double
settlement refused; filing blocked by pause / solvency / cooldown /
duplicate claim / 3-per-address; dial changes not touching open
challenges; pool one-way valve (no path out but bounties);
callback caller spoofing refused; fee-change mid-flight harmless.

## 10. Delivery and acceptance

Build → Foundry tests green → adversarial audit (different seats)
→ deploy to mainnet with the constructor params above → source
verified on the public explorer → delivery repo with contract,
tests, audit findings and deployment record. Acceptance: all tests
listed in §9 present and passing; audit findings answered or fixed;
the deployed bytecode matches the delivered source; owner is the
newsroom wallet; a first staged challenge on a known-false test
claim settles correctly end to end (this doubles as the
Intake.request() live proof).

## 11. Out of scope for the build job

The /disputes page and TRIAL badge (site work, ours); publishing
the rubric (deferred by her call until the desk ships); the
independent post-delivery audit job (separate 0.5 IMD mint); pool
seeding (a fundPool call from the newsroom wallet after deploy:
4.5 IMD, her number 2026-11-11 — three upholds deep).

## Open dials — ALL DECIDED (her numbers, 2026-11-11)
1. ✓ Cooldown after a rejected claim = 7 days.
2. ✓ Panel size/quorum = 5/3.
3. ✓ Pool seed at deploy = 4.5 IMD (three upholds deep; her pick
   over the 3 IMD proposal).

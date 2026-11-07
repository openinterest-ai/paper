Ethereum’s censorship guarantee has an eligibility test.

STANDFIRST

Thomas Thiery’s draft EIP-8369 would leave transactions outside two defined profiles without enforced inclusion. [https://eips.ethereum.org/EIPS/eip-8369] The inference is that wallet validation, storage and payment design would help determine censorship protection, alongside validator conduct. [https://eips.ethereum.org/EIPS/eip-8369] That is a consequence of proposed rules, not evidence of censorship already occurring. [https://eips.ethereum.org/EIPS/eip-8369]

The exception gets its own heading.

Thomas Thiery, the author of EIP-8369, gives excluded transactions a separate heading in his specification. [https://eips.ethereum.org/EIPS/eip-8369] Under “Transactions outside FOCIL enforcement”, the document lists transaction shapes and validation dependencies that would receive no compulsory inclusion. [https://eips.ethereum.org/EIPS/eip-8369] A transaction could reach an inclusion list and still fall outside the proposed protection. [https://eips.ethereum.org/EIPS/eip-8369]

The distinction matters because inclusion lists promise something valuable: a route past a builder that would prefer to omit a transaction. [https://eips.ethereum.org/EIPS/eip-7805] Builders assemble the transactions in a block; inclusion lists would let committees of validators constrain that choice. [https://eips.ethereum.org/EIPS/eip-7805] The proposed protection transfers some authority over admission from a block’s assembler to other network participants. [https://eips.ethereum.org/EIPS/eip-7805]

Ethereum.org places that promise beside a second change on its Hegotá roadmap, updated on 16 October 2026. [https://ethereum.org/roadmap/hegota/] It schedules both inclusion lists and frame transactions, which let accounts define their own validation logic. [https://ethereum.org/roadmap/hegota/] The page describes the upgrade as being in planning and gives April–June 2027 as an unconfirmed mainnet expectation. [https://ethereum.org/roadmap/hegota/]

Those changes address different powers: who can demand a transaction’s inclusion, and what can make a transaction valid. [https://eips.ethereum.org/EIPS/eip-7805] [https://eips.ethereum.org/EIPS/eip-8141] Their intersection is the subject of Thiery’s draft, whose creation date is 5 August 2026. [https://eips.ethereum.org/EIPS/eip-8369] Programmable validation expands what accounts can require, but enforcing inclusion requires other participants to reproduce those checks within bounded resources. [https://eips.ethereum.org/EIPS/eip-8369]

On 7 September 2026, the Ethereum Foundation’s Protocol cluster identified that interaction as central engineering work for Hegotá. [https://blog.ethereum.org/2026/09/07/protocol-priorities] Its priorities document said client teams could begin implementation late in October–December 2026. [https://blog.ethereum.org/2026/09/07/protocol-priorities] That was an implementation prospect, distinct from the roadmap’s unconfirmed activation expectation. [https://blog.ethereum.org/2026/09/07/protocol-priorities] [https://ethereum.org/roadmap/hegota/]

EIP-8369 does not settle that engineering work by existing. [https://eips.ethereum.org/EIPS/eip-8369] It is a draft Informational proposal, and a future Standards Track extension must establish the binding enforcement rules. [https://eips.ethereum.org/EIPS/eip-8369] The boundary is documented; the consensus mechanism that would enforce this version remains work to specify. [https://eips.ethereum.org/EIPS/eip-8369]

An inclusion list is a conditional demand.

Fork-choice enforced inclusion lists, abbreviated FOCIL, would let a validator committee publish transactions for a subsequent block. [https://eips.ethereum.org/EIPS/eip-7805] Attesters, the validators casting votes on blocks, would check the lists they stored before voting. [https://eips.ethereum.org/EIPS/eip-7805] Their refusal to vote would enforce the inclusion conditions. [https://eips.ethereum.org/EIPS/eip-7805]

EIP-7805 specifies 16 committee members, each with a list capped at 8 KiB of encoded transactions. [https://eips.ethereum.org/EIPS/eip-7805] Those are separate lists, rather than a single builder’s selection, but each remains small and finite. [https://eips.ethereum.org/EIPS/eip-7805] Implementers retain discretion over list construction, including selection by fee, waiting time or random choice. [https://eips.ethereum.org/EIPS/eip-7805]

The draft leaves two important exits from the obligation. [https://eips.ethereum.org/EIPS/eip-7805] A builder can omit a listed transaction if it would be invalid after the block’s transactions execute. [https://eips.ethereum.org/EIPS/eip-7805] Omission is also permitted when the remaining block gas cannot accommodate its declared gas requirement. [https://eips.ethereum.org/EIPS/eip-7805]

Gas measures and limits execution resources; it makes the demand conditional on available block capacity. [https://eips.ethereum.org/EIPS/eip-7805] A transaction’s presence on a list therefore would not reserve space or guarantee successful application execution. [https://eips.ethereum.org/EIPS/eip-7805] The check asks whether omission remains justified under specified conditions. [https://eips.ethereum.org/EIPS/eip-7805]

Thiery’s eligibility proposal adds a distinction that a wallet’s ordinary submission process could obscure. [https://eips.ethereum.org/EIPS/eip-8369] A mempool is a transaction pool from which pending transactions can reach builders or inclusion-list participants. [https://eips.ethereum.org/EIPS/eip-7805] Acceptance into the public pool and eligibility for enforcement are separate decisions under EIP-8369. [https://eips.ethereum.org/EIPS/eip-8369]

The document explicitly permits a transaction to pass either check, both checks or neither. [https://eips.ethereum.org/EIPS/eip-8369] An eligible transaction could arrive through a custom pool or direct submission instead of the public pool. [https://eips.ethereum.org/EIPS/eip-8369] Conversely, public propagation would not itself establish an enforceable inclusion claim. [https://eips.ethereum.org/EIPS/eip-8369]

Even list propagation does not certify every enclosed transaction. [https://eips.ethereum.org/EIPS/eip-7805] EIP-7805’s forwarding checks authenticate the list and constrain its size without execution-layer validation of each transaction. [https://eips.ethereum.org/EIPS/eip-7805] A list may therefore carry invalid transactions as well as valid ones. [https://eips.ethereum.org/EIPS/eip-7805]

Direct submission also depends on someone receiving it. [https://eips.ethereum.org/EIPS/eip-8369] Thiery warns that a transaction unseen by every includer cannot receive FOCIL enforcement, whatever its technical eligibility. [https://eips.ethereum.org/EIPS/eip-8369] The document identifies denial-of-service, metadata and private-access-market risks around direct endpoints. [https://eips.ethereum.org/EIPS/eip-8369]

The inference is that a custom route could solve a propagation restriction while creating a separate question about committee access. [https://eips.ethereum.org/EIPS/eip-8369] Eligibility would describe the transaction, while visibility would still depend on its route to an includer. [https://eips.ethereum.org/EIPS/eip-8369] Neither condition alone supplies the full chain from submission to enforced inclusion. [https://eips.ethereum.org/EIPS/eip-8369]

These distinctions resist a simple status label: received, propagated, listed and enforceable describe different conditions in the proposals. [https://eips.ethereum.org/EIPS/eip-7805] [https://eips.ethereum.org/EIPS/eip-8369] The inference for wallet communication is significant: a successful submission response could establish delivery without establishing protection. [https://eips.ethereum.org/EIPS/eip-8369] A transaction can be visible to the mechanism without qualifying for its remedy. [https://eips.ethereum.org/EIPS/eip-8369]

The wallet carries part of the boundary.

EIP-8369 organises eligibility around validity-only partial statelessness, or VOPS: retaining selected state needed to check transaction validity. [https://eips.ethereum.org/EIPS/eip-8369] Its first profile covers legacy transactions and the types specified by EIP-2930, EIP-1559 and EIP-7702. [https://eips.ethereum.org/EIPS/eip-8369] These retain the end-of-block omission check, based on sender state, fees and remaining gas. [https://eips.ethereum.org/EIPS/eip-8369]

For this profile, eligibility checks classify the sender’s code without executing it. [https://eips.ethereum.org/EIPS/eip-8369] Accounts with empty code and valid EIP-7702 delegation indicators can originate these transactions under the stated conditions. [https://eips.ethereum.org/EIPS/eip-8369] The proposal therefore does not divide protection neatly between every simple wallet and every programmable wallet. [https://eips.ethereum.org/EIPS/eip-8369]

The second profile addresses frame transactions under EIP-8141. [https://eips.ethereum.org/EIPS/eip-8369] Frames are contract calls that separate validation, payment approval and application operations within a transaction. [https://eips.ethereum.org/EIPS/eip-8141] Account abstraction means an account’s code can define authorisation and payment instead of relying exclusively on a fixed signature rule. [https://eips.ethereum.org/EIPS/eip-8141]

Profile 2 restricts the state those preliminary checks can consult. [https://eips.ethereum.org/EIPS/eip-8369] It permits specified account fields, code, keyed nonce state, recent roots and a small initial range of sender and payer storage slots. [https://eips.ethereum.org/EIPS/eip-8369] A storage slot is an indexed location holding contract state; the eligible range would start at slot zero. [https://eips.ethereum.org/EIPS/eip-8369]

The draft suggests two to four initial slots, while leaving the final count to the enforcing proposal and benchmarks. [https://eips.ethereum.org/EIPS/eip-8369] It explicitly says Profile 2 cannot be classified for enforcement until that value is selected. [https://eips.ethereum.org/EIPS/eip-8369] The candidate range describes an unresolved design choice, rather than a wallet compatibility specification ready for deployment. [https://eips.ethereum.org/EIPS/eip-8369]

The restriction concerns validation, not every application operation following payment approval. [https://eips.ethereum.org/EIPS/eip-8141] EIP-8141 separates its validation prefix, the preliminary frames ending when a payer is established, from the subsequent execution body. [https://eips.ethereum.org/EIPS/eip-8141] That distinction prevents an overstatement: accessing complicated application state does not automatically place every transaction outside the proposed profiles. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8141]

But consulting the wrong state during validation would matter. [https://eips.ethereum.org/EIPS/eip-8369] EIP-8369 excludes arbitrary external storage, ordinary privacy-contract mappings and storage locations derived through hashing outside the permitted surface. [https://eips.ethereum.org/EIPS/eip-8369] Its examples include proxy slots and namespaced state, both excluded when outside the permitted storage range. [https://eips.ethereum.org/EIPS/eip-8369]

A hypothetical wallet could implement an authorisation check through allowed low-numbered slots or through an excluded external mapping. [https://eips.ethereum.org/EIPS/eip-8369] The inference is that similar user-facing functions could receive different protection because their validation reads differ. [https://eips.ethereum.org/EIPS/eip-8369] No named wallet has been tested here, and the draft supplies no application compatibility census. [https://eips.ethereum.org/EIPS/eip-8369]

Code sharing does not automatically create the same exclusion as shared mutable storage. [https://eips.ethereum.org/EIPS/eip-8369] Profile 2 retains code reached during validation, authenticated through its code hash, and permits shared verifier contracts within its state restrictions. [https://eips.ethereum.org/EIPS/eip-8369] The boundary concerns the verifier’s dependencies as well as the verifier’s existence. [https://eips.ethereum.org/EIPS/eip-8369]

Other exclusions are categorical within this reference model. [https://eips.ethereum.org/EIPS/eip-8369] Blob transactions and frame transactions carrying blobs fall outside both profiles because the draft provides no omission check for the separate blob-gas budget. [https://eips.ethereum.org/EIPS/eip-8369] Bounded validation would determine eligibility before any question about a builder’s motives arose. [https://eips.ethereum.org/EIPS/eip-8369]

The builder can choose the moment of judgment.

The second profile changes more than the permitted storage. [https://eips.ethereum.org/EIPS/eip-8369] For an omitted frame transaction, the builder could commit a transaction index at which validators evaluate the omission. [https://eips.ethereum.org/EIPS/eip-8369] That index identifies a position before, between or after the transactions already in the block. [https://eips.ethereum.org/EIPS/eip-8369]

Attesters would reconstruct the state at that position and replay the listed transaction’s validation. [https://eips.ethereum.org/EIPS/eip-8369] They would check eligibility, fee validity, list-budget admission and whether its gas limit fits the capacity remaining there. [https://eips.ethereum.org/EIPS/eip-8369] A missing, malformed or out-of-range index would default to the end of the block. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery’s security section states the consequence directly: the builder chooses the index, so protection requires validity at every claimable index. [https://eips.ethereum.org/EIPS/eip-8369] The chosen index is not evidence that the builder attempted insertion. [https://eips.ethereum.org/EIPS/eip-8369] The rule would permit a justification based on a position, without requiring a history of failed attempts. [https://eips.ethereum.org/EIPS/eip-8369]

The document gives a queued transaction as an example of weaker protection. [https://eips.ethereum.org/EIPS/eip-8369] A nonce, a replay-protection sequence number, may require a predecessor transaction to execute first. [https://eips.ethereum.org/EIPS/eip-8250] Such a transaction can be invalid before its predecessor and valid afterward, leaving an earlier index available to justify omission. [https://eips.ethereum.org/EIPS/eip-8369]

A shared payer creates another dependency. [https://eips.ethereum.org/EIPS/eip-8369] Another sponsored transaction could reduce that payer’s balance before the builder’s claimed position, weakening protection unless payment capacity is reserved for the transaction. [https://eips.ethereum.org/EIPS/eip-8369] The relevant question would concern available funds at the chosen state, rather than the transaction’s earlier appearance of validity. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery distinguishes dependencies that remain constant or change monotonically within a block. [https://eips.ethereum.org/EIPS/eip-8369] Monotonic change here means invalidity, once established, persists to the end rather than turning back into validity. [https://eips.ethereum.org/EIPS/eip-8369] For position-stable transactions, the draft says the guarantee matches EIP-7805’s end-of-payload rule. [https://eips.ethereum.org/EIPS/eip-8369]

This qualification keeps the argument from becoming an accusation. [https://eips.ethereum.org/EIPS/eip-8369] The proposal openly accepts the trade between replay cost and guarantee strength. [https://eips.ethereum.org/EIPS/eip-8369] Its examples describe permitted outcomes under draft rules, not observations of builders exploiting deployed enforcement. [https://eips.ethereum.org/EIPS/eip-8369]

For the person relying on a sponsored wallet, the inferred consequence is nevertheless concrete. [https://eips.ethereum.org/EIPS/eip-8369] Protection could depend on whether another transaction can spend the same payment capacity or alter an authorisation dependency. [https://eips.ethereum.org/EIPS/eip-8369] Validator willingness alone could not make those dependencies disappear from the omission check. [https://eips.ethereum.org/EIPS/eip-8369]

Privacy gets a narrow route through.

Recent roots offer one proposed way to consult application state without opening arbitrary storage to validation. [https://eips.ethereum.org/EIPS/eip-8272] A root is a compact commitment to a larger state structure; EIP-8272 cites privacy commitment trees as an application. [https://eips.ethereum.org/EIPS/eip-8272] A spend could refer to a recorded root instead of directly reading that tree’s mutable storage during validation. [https://eips.ethereum.org/EIPS/eip-8272]

EIP-8272 provides a shared contract for publishing roots and a standard verification frame for checking them. [https://eips.ethereum.org/EIPS/eip-8272] Its frame identifies each reference through a source, slot and root, allowing clients to track the dependency. [https://eips.ethereum.org/EIPS/eip-8272] The source distinguishes the writer and its chosen root stream. [https://eips.ethereum.org/EIPS/eip-8272]

A root written in one slot becomes referenceable in the next, rather than during the slot containing its write. [https://eips.ethereum.org/EIPS/eip-8272] Each source has an 8,192-entry rolling window, of which 8,191 prior slots are usable because the current slot is excluded. [https://eips.ethereum.org/EIPS/eip-8272] That arrangement prevents current-slot writes from overwriting references still eligible for use, except through a chain reorganisation. [https://eips.ethereum.org/EIPS/eip-8272]

A reorganisation can remove a referenced entry, requiring clients to recheck affected transactions. [https://eips.ethereum.org/EIPS/eip-8272] The root check also proves less than an application’s full claim: it establishes that the specified tuple is stored and recent. [https://eips.ethereum.org/EIPS/eip-8272] Applications remain responsible for what the root represents and for binding it to the authorised action. [https://eips.ethereum.org/EIPS/eip-8272]

Keyed nonces address a separate privacy dependency: many users sharing a sender without sharing one mandatory transaction sequence. [https://eips.ethereum.org/EIPS/eip-8250] A nonce key selects an independent replay-protection domain, allowing disjoint key sets to avoid invalidating one another through a shared sequence. [https://eips.ethereum.org/EIPS/eip-8250] The proposal cites keys derived from nullifiers, identifiers used to prevent a privacy spend from being repeated. [https://eips.ethereum.org/EIPS/eip-8250]

That protocol capability does not itself establish unrestricted public-pool concurrency. [https://eips.ethereum.org/EIPS/eip-8250] EIP-8250 preserves EIP-8141’s one-pending-frame-transaction-per-sender public-mempool limit. [https://eips.ethereum.org/EIPS/eip-8250] The distinction again places transaction semantics and distribution policy on separate tracks. [https://eips.ethereum.org/EIPS/eip-8250]

Publication itself remains a separate inclusion problem. [https://eips.ethereum.org/EIPS/eip-8272] EIP-8272 does not guarantee that a root-writing transaction enters a block, and it leaves timely publication paths to applications. [https://eips.ethereum.org/EIPS/eip-8272] A spend cannot obtain a usable reference merely because its intended root is ready offchain. [https://eips.ethereum.org/EIPS/eip-8272]

The inference is that privacy protection would involve both recording the commitment and qualifying the subsequent spend. [https://eips.ethereum.org/EIPS/eip-8272] A successful recent-root check would address the latter transaction’s state dependency without retroactively guaranteeing publication of the former. [https://eips.ethereum.org/EIPS/eip-8272] This narrows what the proposed root mechanism can establish for an application. [https://eips.ethereum.org/EIPS/eip-8272]

The published drafts also require care when read together. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272] EIP-8369’s shape-matching rule explicitly skips an optional expiry frame, while EIP-8272 adds a leading recent-root verifier and instructs public-pool clients to skip both. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272] The texts do not establish that the added frame fits the eligibility grammar without further composition. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272]

There is a second difference in the nonce examples. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8250] EIP-8369 describes single-use nullifiers with nonce_seq equal to zero; EIP-8250 reserves MAX_NONCE_SEQ for its explicitly single-use form. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8250] Zero in EIP-8250 instead permits a first sequential use of an unused key. [https://eips.ethereum.org/EIPS/eip-8250]

These are document differences, not an execution test proving incompatibility. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8250] [https://eips.ethereum.org/EIPS/eip-8272] EIP-8369 itself requires a composed encoding and signature specification before activation. [https://eips.ethereum.org/EIPS/eip-8369] The privacy route is a proposed design whose joins still need definition. [https://eips.ethereum.org/EIPS/eip-8369]

The limit protects the people doing the checking.

The strongest defence of this boundary comes from Thiery’s own rationale: unrestricted programmable validation would make compulsory checks expensive. [https://eips.ethereum.org/EIPS/eip-8369] EIP-8141 separately describes how an attacker could invalidate many pending transactions by changing one shared dependency. [https://eips.ethereum.org/EIPS/eip-8141] Programmability creates work for validators and transaction-pool operators as well as options for wallet designers. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8141]

The claimed-index design avoids an earlier iterative append process that could require quadratic work as transactions made other transactions valid. [https://eips.ethereum.org/EIPS/eip-8369] One replay position per omitted transaction limits that particular source of repeated checking. [https://eips.ethereum.org/EIPS/eip-8369] The resulting weaker protection is an acknowledged engineering exchange. [https://eips.ethereum.org/EIPS/eip-8369]

The candidate validation allowance is about 1.05 million gas per inclusion list, pending benchmarks. [https://eips.ethereum.org/EIPS/eip-8369] Across 16 includers, the draft calculates about 16.8 million gas per slot in metered Profile 2 work. [https://eips.ethereum.org/EIPS/eip-8369] These are proposed checking budgets, distinct from the 100,000-gas public-mempool validation allowance described in EIP-8141. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8141]

List membership also does not bypass the proposed checking allowance. [https://eips.ethereum.org/EIPS/eip-8369] Profile 2 budget admission follows list order, with each occurrence evaluated before duplicate transactions are removed. [https://eips.ethereum.org/EIPS/eip-8369] An enforceable transaction needs at least one occurrence admitted under that procedure, as well as eligibility at the evaluation state. [https://eips.ethereum.org/EIPS/eip-8369]

The budget calculation uses signature costs and declared validation limits, rather than promising space according to an anticipated successful execution. [https://eips.ethereum.org/EIPS/eip-8369] Invalid signatures still consume their signature-checking debit, while a candidate failing after that stage can retain the larger debit. [https://eips.ethereum.org/EIPS/eip-8369] The draft uses those rules to bound checking work even when a list contains unsuccessful candidates. [https://eips.ethereum.org/EIPS/eip-8369]

Even those figures do not measure the complete burden. [https://eips.ethereum.org/EIPS/eip-8369] Thiery requires benchmarks covering state reconstruction, replay and code loading against the attestation deadline. [https://eips.ethereum.org/EIPS/eip-8369] Omitted transactions pay no fees, and execution gas alone does not bound every byte of code validators might load. [https://eips.ethereum.org/EIPS/eip-8369]

The draft also concedes that retaining specified kinds of state does not cap their aggregate size. [https://eips.ethereum.org/EIPS/eip-8369] Code, keyed nonce entries, recent-root sources and low-numbered storage can all grow. [https://eips.ethereum.org/EIPS/eip-8369] Affordability therefore remains a benchmark and storage question, rather than a result demonstrated by the proposed numerical limits. [https://eips.ethereum.org/EIPS/eip-8369]

Consensus integration contains another unresolved dependency. [https://eips.ethereum.org/EIPS/eip-8369] Under the proposer-builder separation described in EIP-8369, payloads become available after beacon attestations, while this framework assumes payload execution precedes omission checks. [https://eips.ethereum.org/EIPS/eip-8369] The enforcing extension would need a post-reveal checking duty or would leave Profile 2 disabled in that setting. [https://eips.ethereum.org/EIPS/eip-8369]

The Protocol cluster wants inclusion lists and frames tested together; the roadmap still lists keyed nonces and recent roots as proposals under consideration. [https://blog.ethereum.org/2026/09/07/protocol-priorities] [https://ethereum.org/roadmap/hegota/] Those records express priorities and scope status, not deployed performance or a catalogue of qualifying applications. [https://blog.ethereum.org/2026/09/07/protocol-priorities] [https://ethereum.org/roadmap/hegota/]

No interviews or application tests supplement the documents here. The missing evidence includes implementation benchmarks and named wallets’ behaviour under a final composed specification. [https://eips.ethereum.org/EIPS/eip-8369] Thiery’s recorded rationale supplies the defence of the limits; no separate response to this feature was sought.

The inference that remains is narrower than a general verdict on Ethereum’s censorship resistance. [https://eips.ethereum.org/EIPS/eip-8369] If these profiles govern enforcement, wallet architecture would help decide which transactions can invoke it. [https://eips.ethereum.org/EIPS/eip-8369] Changing the pool through which a transaction travels would not erase an excluded validation dependency. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery’s exception heading is therefore a useful place to return. [https://eips.ethereum.org/EIPS/eip-8369] Outside both profiles, a transaction could still find a willing builder and enter a block. [https://eips.ethereum.org/EIPS/eip-8369] Under his reference model, the committee could carry that transaction on its list without gaining the power to compel its inclusion. [https://eips.ethereum.org/EIPS/eip-8369]

SOURCES

Thomas Thiery, EIP-8369: VOPS Profiles for FOCIL Eligibility; draft Informational reference model, including its security and extension requirements. [https://eips.ethereum.org/EIPS/eip-8369]

Thomas Thiery and co-authors, EIP-7805: Fork-choice enforced Inclusion Lists; draft committee, omission and voting rules. [https://eips.ethereum.org/EIPS/eip-7805]

Ethereum.org, Hegotá roadmap; page update dated 16 October 2026, including scheduled changes and unsettled supporting proposals. [https://ethereum.org/roadmap/hegota/]

Ethereum Foundation Protocol Cluster, EF Protocol: Current and Emerging Priorities, 7 September 2026; implementation expectations and joint testing commitment. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

Thomas Thiery and co-authors, EIP-8272: Recent Roots for Frame Transactions; root publication, verification, expiry and public-mempool rules. [https://eips.ethereum.org/EIPS/eip-8272]

Vitalik Buterin and co-authors, EIP-8141: Frame Transaction; frame execution, validation prefixes, payment and public-mempool policy. [https://eips.ethereum.org/EIPS/eip-8141]

Thomas Thiery and co-authors, EIP-8250: Keyed Nonces for Frame Transactions; nonce domains, single-use encoding and retained public-pool limit. [https://eips.ethereum.org/EIPS/eip-8250]

METHOD

The document sweep on 7 November 2026 covered the seven listed primary sources and the house feature register. [https://raw.githubusercontent.com/openinterest-ai/paper/main/style-guide.html] It compared eligibility, omission, validation and supporting-state rules, cutting detailed opcode mechanics, unrelated upgrade candidates, quantum forecasts and claims of existing censorship. [https://eips.ethereum.org/EIPS/eip-8369] No secondary reporting, private sources, interviews, chain measurements or application tests were used; prospective consequences remain inferences, and draft differences establish no deployed failure.

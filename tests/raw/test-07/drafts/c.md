Ethereum’s censorship guarantee has an eligibility test.

STANDFIRST

Ethereum’s proposed inclusion guarantee would depend partly on how wallets validate transactions, an inference from Thomas Thiery’s eligibility draft. Transactions outside its two profiles could reach an inclusion list without gaining enforced inclusion. The draft describes a possible boundary, not evidence that censorship has occurred. [https://eips.ethereum.org/EIPS/eip-8369]

The exception in Thiery’s document

Thomas Thiery’s name sits above a table with two rows: one for familiar transaction formats, another for programmable validation. Below it, his draft identifies transactions that would receive no inclusion enforcement. Its title is EIP-8369, VOPS Profiles for FOCIL Eligibility. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery is also among the authors of EIP-7805, the inclusion-list proposal whose protection his later document qualifies. That proposal gives validators a way to constrain which transactions builders leave out. The same documentary record contains the promise and its boundary. [https://eips.ethereum.org/EIPS/eip-7805] [https://eips.ethereum.org/EIPS/eip-8369]

The promise concerns an ordinary act: getting a submitted transaction into a block despite a builder’s preferences. EIP-7805 proposes committees whose lists would constrain builders, with other validators checking compliance before voting. Its authors attribute the need to concentrated block production and the resulting deterioration of censorship resistance. [https://eips.ethereum.org/EIPS/eip-7805]

That is the authors’ diagnosis, not an independently measured finding in this report. Their proposed remedy would give transactions another route into blocks beyond voluntary builder selection. For someone relying on a wallet, the relevant distinction is whether refusal can carry a protocol consequence. [https://eips.ethereum.org/EIPS/eip-7805]

EIP-8369 makes that consequence conditional on the transaction’s design. It calls itself informational and nonbinding, requiring a future consensus extension to turn its reference model into enforcement. Its creation date is 5 August 2026; the document does not itself change Ethereum’s rules. [https://eips.ethereum.org/EIPS/eip-8369]

The timing nevertheless makes the boundary consequential. Ethereum.org’s Hegotá page, updated on 16 October 2026, lists inclusion lists and frame transactions as scheduled changes. It describes an upgrade still in planning, with mainnet expected in the second quarter of 2027 and no confirmed date. [https://ethereum.org/roadmap/hegota/]

Frame transactions would let accounts run their own verification logic, including arrangements for recovery, multiple approvals and another party paying fees. The roadmap lists supporting proposals, including recent roots and keyed nonces, as under consideration rather than settled. Scheduling the main changes therefore does not settle every dependency beneath them. [https://ethereum.org/roadmap/hegota/]

The Ethereum Foundation’s Protocol cluster makes the relationship explicit in its priorities dated 7 September 2026. It says inclusion lists and frame transactions must ship safely together, with their interaction tested. Client teams could realistically begin Hegotá implementation in late 2026, according to that statement; implementation is not mainnet activation. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

The feature’s inference follows from those documents: validator honesty would remain necessary, but would not determine protection alone. Wallet validation would also determine which omissions the protocol could punish. A wallet could produce an executable transaction without producing an enforceable demand for inclusion. [https://eips.ethereum.org/EIPS/eip-8369]

A list is not a receipt

An inclusion list is a validator’s proposed set of transactions for a subsequent block. EIP-7805 calls its mechanism fork-choice enforced inclusion lists, shortened to FOCIL. Fork choice determines which chain validators support; here, their votes would depend on satisfying the lists they stored. [https://eips.ethereum.org/EIPS/eip-7805]

The proposal selects a committee of 16 validators rather than assigning list construction to one participant. Each member contributes a list based on its view of pending transactions. Builders collect those lists, and attesters, the validators voting on blocks, check whether the resulting block satisfies them. [https://eips.ethereum.org/EIPS/eip-7805]

The proposal’s honesty assumption concerns committee members, but participation does not erase the remaining conditions. List construction policy stays with implementers, who might select transactions by age, fee or another method. Each list also has an eight-kibibyte size limit, so eligibility does not promise unlimited list space. [https://eips.ethereum.org/EIPS/eip-7805]

Nor must every listed transaction appear in the block. EIP-7805 allows omission when a transaction would be invalid at the block’s end or insufficient gas remains. Gas measures the execution resources charged to transactions; the check prevents a list from demanding execution beyond the block’s allowance. [https://eips.ethereum.org/EIPS/eip-7805]

For the familiar transaction formats, those checks principally concern the sender’s nonce and balance. A nonce is an account’s transaction sequence counter. A transaction can cease to be valid because the sequence has advanced or funds are insufficient when the block finishes. [https://eips.ethereum.org/EIPS/eip-7805]

Thiery’s eligibility draft adds a distinct question before enforcement: whether a transaction fits a supported profile at all. Transactions outside both profiles may still appear on inclusion lists, but their omission is excused. List membership and enforceability therefore describe different things. [https://eips.ethereum.org/EIPS/eip-8369]

The distinction extends to the mempool, the pool of transactions awaiting inclusion. EIP-8369 separates public-mempool admission from FOCIL eligibility, stating that a transaction may pass either check, both or neither. Public admission is not a prerequisite for eligibility. [https://eips.ethereum.org/EIPS/eip-8369]

An includer could receive an eligible transaction through a custom pool or direct submission instead. Conversely, public distribution would not make an otherwise ineligible transaction enforceable. The delivery route determines whether a committee member sees the transaction; the profile determines what follows from its omission. [https://eips.ethereum.org/EIPS/eip-8369]

That separation has a practical limit in the draft’s security discussion. If no includer receives a transaction, FOCIL cannot enforce it. Direct submission also creates potential denial-of-service, private-access-market and metadata risks, which the draft assigns to implementation policy. [https://eips.ethereum.org/EIPS/eip-8369]

These are proposed operating conditions, not a record of a user being denied service. The inference for wallet software is narrower: successful submission would not establish that the transaction has enforcement protection. A pending transaction could have reached willing intermediaries while still lacking a protocol remedy against an unwilling builder. [https://eips.ethereum.org/EIPS/eip-8369]

The wallet’s validation becomes part of the guarantee

The first profile covers legacy transactions and the formats defined by EIP-2930, EIP-1559 and EIP-7702. It checks structural validity, signatures and chain identification where present. Its omission check retains the end-of-block approach, including sender, fee and remaining-gas conditions. [https://eips.ethereum.org/EIPS/eip-8369]

This profile does not execute account code to establish eligibility. It distinguishes empty-code senders and permitted delegated accounts from senders with other code. That matters because the proposal does not simply divide protection between accounts with code and accounts without it. [https://eips.ethereum.org/EIPS/eip-8369]

The second profile covers certain frame transactions, whose validation is programmable. Its technical name, account-abstraction VOPS, describes a limited body of state available for checking those transactions. VOPS means validity-only partial statelessness: retaining the information needed for validity checks without treating all application storage as available. [https://eips.ethereum.org/EIPS/eip-8369]

The permitted information includes account fields, authenticated code, keyed nonce state and recent-root entries. It also includes a small initial range of storage slots belonging to the sender and payer. The proposed range is two to four slots, pending benchmarks and a binding choice in the enforcing proposal. [https://eips.ethereum.org/EIPS/eip-8369]

Those slots are numbered storage locations, not permission to consult any equally small amount of data elsewhere. The draft excludes mappings, proxy slots and namespaced storage at derived locations outside the permitted range. Ordinary external application storage also falls outside the profile. [https://eips.ethereum.org/EIPS/eip-8369]

The restriction applies to validation, the checks that authorize execution and payment. It should not be read as a blanket prohibition on every application interaction the transaction might later execute. The document draws its storage boundary around the validation prefix, the initial sequence of frames performing those checks. [https://eips.ethereum.org/EIPS/eip-8369]

That distinction is central to the wallet argument. An inference from the rules is that two wallets offering similar user-facing functions could receive different enforcement protection. Their validation might consult different storage, even when both transactions remain acceptable to a willing builder. [https://eips.ethereum.org/EIPS/eip-8369]

The draft permits four validation patterns, covering self-verification or separate verification and payment, with optional account deployment. It also restricts flags and later verification frames. Eligibility therefore depends on the transaction’s structure as well as the information its validation reads. [https://eips.ethereum.org/EIPS/eip-8369]

Blob-carrying transactions fall outside both profiles, including frame transactions carrying blobs. The stated reason is a separate blob-gas budget for which this draft supplies no omission check. That exclusion concerns an absent enforcement rule, rather than a finding that the underlying transaction is invalid. [https://eips.ethereum.org/EIPS/eip-8369]

The distinction protects against another overstatement: exclusion would not ban the wallet or its transaction. Builders could still include transactions that fit neither profile. What the wallet would lack under this model is enforced inclusion when the builder declines. [https://eips.ethereum.org/EIPS/eip-8369]

The builder still chooses a testing point

Even a transaction within the second profile faces another qualification. Instead of always testing an omission against the block’s final state, the draft permits a builder-claimed insertion index. That index identifies the point in the block at which validators would evaluate the omitted transaction. [https://eips.ethereum.org/EIPS/eip-8369]

The builder could choose the position before the first transaction, any intervening position or the block’s end. A missing, malformed or out-of-range claim defaults to the end. The index does not prove that the builder actually attempted insertion there. [https://eips.ethereum.org/EIPS/eip-8369]

Attesters would reconstruct the relevant state at that position, replay validation and check fees and available gas. An unjustified omission requires the transaction to satisfy the applicable conditions there. The draft explicitly accepts that builder choice weakens protection for transactions whose validity changes during the block. [https://eips.ethereum.org/EIPS/eip-8369]

Its sequencing example shows the consequence without requiring an allegation of misconduct. A queued transaction might need a predecessor to advance an account’s nonce earlier in the same block. It could then be invalid before that predecessor and valid afterward. [https://eips.ethereum.org/EIPS/eip-8369]

In that example, choosing the earlier position could justify omission despite the transaction becoming valid later. This is a worked implication of the proposed rule, not an observed builder tactic. The document itself classifies such transactions as receiving the weaker guarantee. [https://eips.ethereum.org/EIPS/eip-8369]

Sponsorship provides another example close to the wallet user. The draft says a shared payer without reserved payment capacity receives weaker protection. Another sponsored transaction could reduce that payer’s balance before the builder’s chosen testing point. [https://eips.ethereum.org/EIPS/eip-8369]

The inference is that offering fee sponsorship would not, by itself, establish equivalent censorship protection for every sponsored payment. Reservation of payment capacity and the behavior of other transactions would matter. The relevant design choice could sit behind a wallet’s payment arrangement rather than in its visible approval screen. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery’s draft contrasts these cases with dependencies it calls position-stable. These remain constant within the block, or change so that invalidity at an earlier point persists to the end. For such transactions, the claimed-index approach is equivalent to the original end-of-block rule. [https://eips.ethereum.org/EIPS/eip-8369]

Fresh nonzero keyed nonces used once, and recent roots, are the draft’s examples of those dependencies. Validation storage qualifies only if another authorized transaction cannot change it; payment capacity qualifies only when reserved. These qualifications make stability a property to demonstrate, rather than a benefit conferred by the wallet’s label. [https://eips.ethereum.org/EIPS/eip-8369]

The two boundaries should remain separate. Reading excluded storage can put a transaction outside enforcement entirely, while changing permitted state can weaken an otherwise eligible transaction’s protection. Under this model, a willing includer cannot remove either limitation merely by putting the transaction on a list. [https://eips.ethereum.org/EIPS/eip-8369]

Privacy needs a stable reference and a publication path

Privacy transactions are a motivating case inside EIP-8369, not simply an excluded category. The draft describes a spend that checks recent roots and consumes single-use keyed nonces. Its proposed path avoids consulting unrestricted privacy-contract storage during validation. [https://eips.ethereum.org/EIPS/eip-8369]

A recent root represents a recorded commitment to application state. EIP-8272, co-authored by Thiery, describes privacy applications proving spends against such commitments. Its mechanism would let a frame transaction verify a recorded root before account validation runs. [https://eips.ethereum.org/EIPS/eip-8272]

The verification frame carries between one and 16 references, each specifying a source, slot and root. A contract checks those references against stored entries. Applications can then inspect the completed verification frame through the frame-transaction machinery. [https://eips.ethereum.org/EIPS/eip-8272]

The mechanism deliberately uses past slots rather than the current slot’s still-changing entry. A root written during one slot becomes referenceable from the next, with the final write determining that slot’s root. This gives validation a historical reference whose value cannot change during its usable period, except through a chain reorganization. [https://eips.ethereum.org/EIPS/eip-8272]

The proposed storage cycle contains 8,192 positions per source, while references remain usable for 8,191 slots. The age checks exclude the current slot and reject expired references even if an old storage entry remains. The transaction pool must evict references once they pass the permitted age. [https://eips.ethereum.org/EIPS/eip-8272]

This is a limited statement about recorded data. EIP-8272 says successful verification establishes that a tuple is stored and recent; the application defines its meaning. Application validation must still bind the expected reference to the action being authorized. [https://eips.ethereum.org/EIPS/eip-8272]

EIP-8369 adds corresponding responsibilities for privacy proofs. The proof must authenticate the sender, nonce keys, precise root references, chain and contract domain, and intended execution and payment. An eligible validation path would not excuse a privacy protocol from checking what its proof actually authorizes. [https://eips.ethereum.org/EIPS/eip-8369]

Nor does checking a published root guarantee its publication. EIP-8272 expressly provides no inclusion guarantee for root-writing transactions. Applications needing timely roots require their own publication route, redundant sources or an inclusion policy for those writes. [https://eips.ethereum.org/EIPS/eip-8272]

The reviewed texts also leave a question about combining their validation patterns. EIP-8272 explicitly skips the leading root-verification frame when matching patterns; EIP-8369’s pattern rule explicitly skips only the optional expiry frame. EIP-8369 requires a composed encoding and signature hash before activation. [https://eips.ethereum.org/EIPS/eip-8272] [https://eips.ethereum.org/EIPS/eip-8369]

The documents therefore do not establish that combining their rules already yields a finished enforcement implementation. That is an inference from their stated integration requirements, not proof that the approach cannot work. For the privacy-wallet user, the proposed protection reaches through validation design to the transaction that publishes the underlying root. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272]

The cost of making refusal enforceable

The strongest objection to broadening eligibility is already in Thiery’s rationale: enforcement must remain affordable to verify. His draft states, “Profile 2 trades guarantee strength for replay cost.” The claimed-index method replaces an earlier repeated-check approach that could require quadratic builder work. [https://eips.ethereum.org/EIPS/eip-8369]

Quadratic work means checking effort can grow much faster than the number of candidate transactions. EIP-7805 illustrates the problem with transactions that successively fund one another, repeatedly changing which pending transactions become valid. Programmable validation expands the dependencies an enforcement mechanism must handle. [https://eips.ethereum.org/EIPS/eip-7805] [https://eips.ethereum.org/EIPS/eip-8369]

The second profile proposes about 1.05 million verification gas per inclusion list. Across 16 includers, that produces a metered ceiling of about 16.8 million gas per slot. Both are candidate limits requiring benchmarks, rather than measured performance or adopted consensus constants. [https://eips.ethereum.org/EIPS/eip-8369]

The accounting uses declared validation limits plus signature costs, rather than waiting to discover how cheaply validation finishes. Transactions consume a list’s allowance in list order, before duplicate removal. A transaction needs at least one admitted occurrence as well as successful state-dependent checks to receive enforcement. [https://eips.ethereum.org/EIPS/eip-8369]

This creates another distinction from public-mempool admission. The draft identifies a 100,000-gas public-admission limit but says it does not determine the enforcement limits. A larger enforcement allowance would not automatically alter the public pool’s admission policy. [https://eips.ethereum.org/EIPS/eip-8369]

The arithmetic does not settle the operator’s burden. EIP-8369 warns that gas alone does not bound the bytes loaded when validation reaches many large code bodies. Omitted transactions pay no fees, while attesters still perform reconstruction and replay within their deadline. [https://eips.ethereum.org/EIPS/eip-8369]

The storage boundary also limits categories of data rather than total stored volume. Code, keyed nonces, root sources and permitted account slots can grow. The draft therefore requires benchmarks and parameter choices covering storage growth as well as replay time. [https://eips.ethereum.org/EIPS/eip-8369]

That reasoning deserves concession: unrestricted validation would not provide an equally cheap enforcement promise. The tradeoff could protect validator participation while narrowing transaction coverage. Whether these particular limits achieve that balance remains an implementation question the draft explicitly leaves to benchmarks. [https://eips.ethereum.org/EIPS/eip-8369]

Consensus integration adds a timing problem beyond wallet design. The draft says the proposed separation of proposers and builders reveals payloads after beacon attestations. Under that arrangement, omission checks must move to a duty after revelation, or the second profile must remain disabled. [https://eips.ethereum.org/EIPS/eip-8369]

No wallet inventory, client benchmark or deployment test accompanies this report’s document analysis. The reviewed specifications establish neither which named applications would qualify nor how quickly their transactions would arrive. Those questions require implementation evidence and application-level reporting beyond the documents’ proposed conditions. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery’s table thus returns the question to the transaction a wallet creates. A future extension could make an eligible omission grounds for withholding votes, while an excluded transaction could still depend on voluntary inclusion. The same committee could see both transactions, and owe them different protection. [https://eips.ethereum.org/EIPS/eip-8369]

SOURCES

Thomas Thiery, EIP-8369: VOPS Profiles for FOCIL Eligibility, draft informational proposal created 5 August 2026. Eligibility, state restrictions, claimed-index checks, budgets and activation requirements. [https://eips.ethereum.org/EIPS/eip-8369]

Thomas Thiery and co-authors, EIP-7805: Fork-choice enforced Inclusion Lists, draft core proposal created 1 November 2024. Committee design, omission conditions, list limits and builder-work rationale. [https://eips.ethereum.org/EIPS/eip-7805]

Thomas Thiery, Vitalik Buterin, Toni Wahrstätter and lightclient, EIP-8272: Recent Roots for Frame Transactions, draft core proposal created 15 May 2026. Root verification, reference lifetime, application responsibilities and publication limits. [https://eips.ethereum.org/EIPS/eip-8272]

Ethereum.org, Hegotá roadmap, page update dated 16 October 2026. Scheduled changes, planning status and unsettled supporting proposals. [https://ethereum.org/roadmap/hegota/]

Ethereum Foundation Protocol Cluster, EF Protocol: Current and Emerging Priorities, 7 September 2026. Implementation timing and the requirement to test inclusion lists with frame transactions. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

METHOD

The reporting swept the five open primary documents listed above on 7 November 2026, including specification, rationale and security sections. It used no secondary reporting or interviews; claims about measured censorship, named-wallet compatibility and deployment performance were cut because the documentary record did not establish them. Wallet consequences and the composition question are marked as inferences; the edit followed the house feature register. [https://raw.githubusercontent.com/openinterest-ai/paper/main/style-guide.html]

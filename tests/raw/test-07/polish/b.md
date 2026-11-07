HEADLINE

Ethereum’s proposed censorship protection starts inside the wallet

STANDFIRST

Thomas Thiery’s draft eligibility rules would let some transactions reach an inclusion list without gaining enforced inclusion. Wallet validation could therefore help determine access to Ethereum’s proposed censorship protection. That is an inference from a reference model, not evidence of censorship under deployed rules. [https://eips.ethereum.org/EIPS/eip-8369]

The exception below the table

Thomas Thiery divides transactions between two rows in his Ethereum proposal. One covers familiar formats; the other covers programmable validation. Below the table, his document identifies transactions whose inclusion the proposed mechanism would not enforce. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery also helped write the proposal whose promise this table qualifies. EIP-7805 would give validator committees a way to constrain block builders, the participants assembling transactions into blocks. Attesters, the validators voting on those blocks, would withhold votes when omissions breach the inclusion rules. [https://eips.ethereum.org/EIPS/eip-7805]

The promise concerns a wallet’s basic purpose: getting an authorized transaction into a block despite a builder’s preference to omit it. EIP-7805’s authors attribute the need to concentrated block production and deteriorating censorship resistance. That is their diagnosis, rather than an independently measured finding in this feature. [https://eips.ethereum.org/EIPS/eip-7805]

Their remedy would give other participants authority over admission. A builder could still assemble the block, but its selection would have to satisfy the committees’ conditions. For someone relying on a wallet, refusal could acquire a protocol consequence. [https://eips.ethereum.org/EIPS/eip-7805]

A separate proposal would expand what that wallet can authorize. Ethereum.org describes frame transactions as supporting account-defined verification, multiple approvals, spending limits and fees paid by another party. Those arrangements let account code determine more of the conditions under which a transaction proceeds. [https://ethereum.org/roadmap/hegota/]

Thiery’s later document brings those promises together. EIP-8369 describes which transactions could receive enforced inclusion when validation extends beyond a fixed signature check. Its exclusions include arbitrary external storage and ordinary privacy-contract storage used during validation. [https://eips.ethereum.org/EIPS/eip-8369]

The resulting inference concerns wallet architecture. Two wallets offering similar approval policies could obtain different protection if their validation consults different data. An honest committee could list both transactions without gaining the same power to compel both into a block. [https://eips.ethereum.org/EIPS/eip-8369]

EIP-8369 is an Informational draft, created on 5 August 2026. It requires a future Standards Track extension to establish binding rules. Its table documents a proposed boundary; it does not change Ethereum’s rules by itself. [https://eips.ethereum.org/EIPS/eip-8369]

The boundary nevertheless sits inside an active engineering programme. Ethereum.org’s Hegotá roadmap, updated on 16 October 2026, schedules inclusion lists and frame transactions together. It describes planning, with an unconfirmed mainnet expectation of April–June 2027. [https://ethereum.org/roadmap/hegota/]

The Ethereum Foundation’s Protocol cluster placed possible client implementation work in late 2026, separately from activation. Its priorities dated 7 September 2026 require inclusion lists and frame transactions to undergo testing together. The question is what protection their combination could promise to the transaction a wallet actually creates. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

What a list can demand

EIP-7805 calls its mechanism fork-choice enforced inclusion lists, abbreviated FOCIL. Fork choice determines which chain validators support; here, their votes would depend on compliance with stored lists. Committee members nominate transactions, builders construct blocks, and attesters check the resulting omissions. [https://eips.ethereum.org/EIPS/eip-7805]

The proposed committee has 16 members, each contributing a list capped at 8 KiB. Selection remains an implementation choice, potentially based on fees, waiting time or random selection. Those paired limits describe several opportunities for nomination, each with finite space. [https://eips.ethereum.org/EIPS/eip-7805]

Nomination would not reserve unconditional execution. EIP-7805 permits omission if a listed transaction would be invalid after the block’s transactions execute. It also permits omission when the transaction’s gas requirement exceeds the block’s remaining allowance. [https://eips.ethereum.org/EIPS/eip-7805]

Gas measures and limits execution resources. A nonce, an account’s transaction sequence counter, and the sender’s balance help determine validity for familiar transaction formats. Another transaction can advance that counter or spend the available funds before the final check. [https://eips.ethereum.org/EIPS/eip-7805]

The list therefore makes a conditional demand. It cannot make an invalid transaction valid, or require a block to exceed its execution allowance. Thiery’s eligibility model adds a prior question: whether the listed transaction belongs to a protected profile at all. [https://eips.ethereum.org/EIPS/eip-7805] [https://eips.ethereum.org/EIPS/eip-8369]

That distinction also separates protection from public distribution. A mempool is a pool of pending transactions that nodes accept and relay. EIP-8369 treats public-mempool admission and enforcement eligibility as independent checks: a transaction can pass either, both or neither. [https://eips.ethereum.org/EIPS/eip-8369]

An eligible transaction could reach an includer through direct submission or a custom pool. Conversely, acceptance into the public pool would not establish that an omission carries an enforcement consequence. Distribution determines who can encounter a transaction; eligibility determines what the mechanism can demand afterward. [https://eips.ethereum.org/EIPS/eip-8369]

Direct access is not an unlimited substitute for public propagation. Thiery’s security discussion identifies denial-of-service, metadata and private-access-market risks around submission endpoints. It also states the practical limit: no enforcement can operate if every includer remains unaware of the transaction. [https://eips.ethereum.org/EIPS/eip-8369]

For a wallet’s user, the inferred distinction is between successful delivery and enforceable inclusion. Submission, circulation, nomination and protection describe separate conditions in these proposals. A transaction can reach willing intermediaries and still lack a remedy against an unwilling builder. [https://eips.ethereum.org/EIPS/eip-8369]

Where the wallet draws its authority

Thiery’s first profile covers legacy transactions and the formats specified by EIP-2930, EIP-1559 and EIP-7702. It retains the end-of-block omission check, using sender state, fees and remaining gas. Eligibility classifies sender code without executing it. [https://eips.ethereum.org/EIPS/eip-8369]

Permitted senders include accounts with empty code and accounts with valid EIP-7702 delegation indicators under the stated conditions. The boundary therefore does not divide every simple account from every programmable account. The validation dependencies determine the classification more precisely than the wallet’s label. [https://eips.ethereum.org/EIPS/eip-8369]

The underlying method is validity-only partial statelessness, or VOPS. Nodes retain selected information needed to check validity rather than consulting unrestricted application state for those checks. The second profile extends that information for programmable frame transactions. [https://eips.ethereum.org/EIPS/eip-8369]

Frames are component contract calls separating validation, payment approval and application operations within a transaction. Account abstraction lets account code define authorization and payment instead of relying exclusively on a fixed signature rule. The additional freedom brings additional information that validators may need to inspect. [https://eips.ethereum.org/EIPS/eip-8141]

Profile 2 permits specified account fields, authenticated code, keyed nonce state and recent roots. It also permits a small initial range of sender and payer storage slots. A slot is an indexed location holding contract state, with the permitted range starting at zero. [https://eips.ethereum.org/EIPS/eip-8369]

The draft suggests two to four initial slots, compared with the arbitrary storage locations it excludes. Benchmarks and the enforcing proposal must settle the count before Profile 2 can be classified for enforcement. This candidate range is not a finished wallet compatibility specification. [https://eips.ethereum.org/EIPS/eip-8369]

The location matters as much as the quantity. Mappings, proxy slots and namespaced storage at hash-derived locations fall outside the profile when outside its permitted range. Reading a small amount of excluded storage would not become acceptable merely because the amount is small. [https://eips.ethereum.org/EIPS/eip-8369]

The restriction concerns validation: the preliminary checks establishing authorization and payment. It does not impose the same small perimeter on every subsequent application operation. Complex application execution alone therefore does not demonstrate that a transaction falls outside enforcement. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8141]

Shared verifier code can remain within the model. Profile 2 retains authenticated code reached during validation while restricting the storage it consults. Calling another contract is consequently different from depending on arbitrary mutable state belonging to that contract. [https://eips.ethereum.org/EIPS/eip-8369]

The inference for wallet design is specific. Similar approval functions might use permitted low-numbered slots in one implementation and an excluded external mapping in another. No named-wallet test or compatibility census in the drafts establishes which products would land on either side. [https://eips.ethereum.org/EIPS/eip-8369]

Other exclusions need no storage comparison. Blob transactions, including frames carrying blobs, fall outside both profiles because the model supplies no omission test for the separate blob-gas budget. Builders could still include them voluntarily; exclusion removes the proposed enforcement claim rather than banning the transaction. [https://eips.ethereum.org/EIPS/eip-8369]

The position the builder can choose

Reaching Profile 2 would not settle the strength of its protection. For an omitted frame transaction, Thiery’s model lets the builder claim an insertion index. That position can lie before the first block transaction, between transactions or at the end. [https://eips.ethereum.org/EIPS/eip-8369]

Attesters would reconstruct the relevant state at that position and replay validation. They would check eligibility, fee validity, budget admission and available gas there. A missing, malformed or out-of-range claim defaults to the block’s end. [https://eips.ethereum.org/EIPS/eip-8369]

The claimed index does not establish that the builder attempted insertion. Thiery’s security discussion states the consequence: protection requires validity at every position the builder could claim. Failure at one position could justify omission even if the transaction could pass elsewhere. [https://eips.ethereum.org/EIPS/eip-8369]

The draft supplies a sequencing example. A queued transaction can require a predecessor to advance its nonce earlier in the same block. It may be invalid before the predecessor and valid afterward, leaving the earlier position available to justify omission. [https://eips.ethereum.org/EIPS/eip-8369]

Fee sponsorship introduces another dependency close to the wallet user. Another sponsored transaction could spend a shared payer’s balance before the selected position. The draft gives payment capacity the stronger stability property only when it is reserved for the transaction. [https://eips.ethereum.org/EIPS/eip-8369]

Validation storage has a similar qualification. Even a permitted slot supplies stability only if another authorized transaction cannot change it. Passing the storage boundary does not remove every source of position-dependent invalidity. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery calls the relevant property position stability. Dependencies remain constant within the block, or change so that invalidity at an earlier position persists through the end. For those transactions, the claimed-index guarantee matches the original end-of-block rule. [https://eips.ethereum.org/EIPS/eip-8369]

These examples describe permitted outcomes under draft rules, not observed tactics under deployed enforcement. The wallet inference is that fee sponsorship and authorization design could affect protection after eligibility is established. Permitted state and stable state are separate requirements, neither supplied by an includer’s willingness to help. [https://eips.ethereum.org/EIPS/eip-8369]

A privacy spend needs an earlier transaction

Privacy is a motivating example inside Thiery’s second profile, rather than simply an excluded application category. The draft describes a spend checking recent roots and consuming a single-use keyed nonce. Its path avoids consulting unrestricted commitment trees or ordinary nullifier mappings during validation. [https://eips.ethereum.org/EIPS/eip-8369]

A root is a compact commitment to a larger body of application state. EIP-8272 describes privacy applications proving spending rights against a recent commitment-tree root. A standard verification frame would check that recorded reference before account validation. [https://eips.ethereum.org/EIPS/eip-8272]

Each reference identifies a source, a slot and a root. The proposed contract checks whether that tuple is stored and recent. Applications still define what the commitment means and must bind the expected reference to the action being authorized. [https://eips.ethereum.org/EIPS/eip-8272]

The mechanism deliberately separates the slot containing a write from the slots allowed to reference it. A root written in one slot becomes usable in the next. Its storage ring contains 8,192 positions per source, while the usable window covers 8,191 prior slots. [https://eips.ethereum.org/EIPS/eip-8272]

Excluding the current slot prevents current writes from overwriting references that remain usable, except through a chain reorganization. Such a reorganization can remove an entry; references also expire as slots advance. Clients must track these dependencies and recheck affected transactions. [https://eips.ethereum.org/EIPS/eip-8272]

Keyed nonces address a different dependency: users sharing a sender without sharing one mandatory transaction sequence. A nonce key selects an independent replay-protection domain. EIP-8250 cites keys derived from nullifiers, identifiers preventing a privacy spend from being repeated. [https://eips.ethereum.org/EIPS/eip-8250]

Independent nonce domains do not themselves establish unrestricted public-pool concurrency. EIP-8250 retains EIP-8141’s one-pending-frame-transaction-per-sender public-mempool limit. The transaction’s replay rules and its distribution policy remain distinct. [https://eips.ethereum.org/EIPS/eip-8250]

The inferred route into protection joins recent commitments with protocol-managed replay checks. It does not establish that an existing privacy application already qualifies. EIP-8369 also requires proofs to authenticate nonce keys, roots, domain, execution and payment intent. [https://eips.ethereum.org/EIPS/eip-8369]

The drafts leave composition questions. EIP-8272’s pattern matching explicitly skips the leading root-verification frame; EIP-8369’s rule explicitly skips only the optional expiry frame. EIP-8369 requires a composed encoding and signature specification before activation. [https://eips.ethereum.org/EIPS/eip-8272] [https://eips.ethereum.org/EIPS/eip-8369]

Those document differences do not constitute an execution test proving incompatibility. They limit the inference to a proposed route whose integration remains unfinished. A specification describing useful components is not evidence that their combined enforcement implementation has passed testing. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272]

There is an earlier dependency that composition alone cannot remove. EIP-8272 expressly gives no inclusion guarantee to the transaction publishing a root. Applications needing timely publication must arrange a publication path, redundant sources or an inclusion policy for those writes. [https://eips.ethereum.org/EIPS/eip-8272]

For the person asking a privacy wallet to spend, the inferred protection thus begins before that request. The commitment must first reach the chain before the spend can refer to it. A mechanism making published roots checkable does not make their publication inevitable. [https://eips.ethereum.org/EIPS/eip-8272]

What the boundary buys

The strongest defence of Thiery’s limits comes from the work they ask validators to perform. Omitted transactions pay no fees, but attesters must still reconstruct state and replay validation within their deadline. Unlimited programmable validation would not deliver an equally cheap enforcement promise. [https://eips.ethereum.org/EIPS/eip-8369]

The claimed-index approach serves that cost argument. It replaces an earlier repeated-append approach that could require quadratic work as transactions make other transactions valid. Checking one claimed position avoids that particular source of repeated work while weakening protection for position-dependent transactions. [https://eips.ethereum.org/EIPS/eip-8369]

The candidate allowance is about 1.05 million verification gas per inclusion list. Across 16 includers, the draft calculates about 16.8 million gas per slot. These paired figures describe proposed workload bounds awaiting benchmarks, not measured performance or adopted constants. [https://eips.ethereum.org/EIPS/eip-8369]

Budget admission follows list order, evaluating occurrences before duplicate removal. Accounting uses declared validation limits and signature costs rather than assuming a cheap successful execution. A transaction needs at least one admitted occurrence as well as successful state-dependent checks. [https://eips.ethereum.org/EIPS/eip-8369]

Even that accounting does not settle the operator’s burden. Gas does not directly bound every byte loaded from distinct code bodies. The enforcing proposal needs code-count and byte limits, with benchmarks covering reconstruction, replay and code loading together. [https://eips.ethereum.org/EIPS/eip-8369]

Restricting categories of retained state also leaves total storage growth unresolved. Code, keyed nonce entries, root sources and permitted account slots can all grow. The draft requires benchmarks and parameter choices rather than treating its storage perimeter as a demonstrated affordability result. [https://eips.ethereum.org/EIPS/eip-8369]

This is a substantive answer to the criticism that wallet design would limit protection. Bounded verification could protect validator participation while narrowing transaction coverage. The documents establish neither that unrestricted enforcement would be safe nor that these particular limits achieve the best balance. [https://eips.ethereum.org/EIPS/eip-8369]

Consensus integration adds a timing condition outside the wallet. Under the proposer-builder separation described in EIP-8369, payloads become available after beacon attestations. The extension must move omission checks to a post-revelation duty or leave Profile 2 disabled in that setting. [https://eips.ethereum.org/EIPS/eip-8369]

The roadmap also leaves recent roots and keyed nonces under consideration rather than settled for delivery. The Protocol cluster’s requirement for joint testing supplies direction, not the missing benchmark results. Scheduling inclusion lists and frames does not establish that every supporting condition is ready. [https://ethereum.org/roadmap/hegota/] [https://blog.ethereum.org/2026/09/07/protocol-priorities]

No interviews, named-wallet tests or client benchmarks supplement the documents carried by these drafts. Thiery’s recorded rationale supplies the defence of the limits; no separate response to the feature was sought. Product compatibility, redesign costs and deployed performance remain outside this evidence. [https://eips.ethereum.org/EIPS/eip-8369]

The supported inference returns to Thiery’s table. A wallet could create a transaction a willing builder can execute, yet fail to create an enforceable demand on an unwilling builder. Validator honesty would remain necessary, but the transaction’s architecture would help determine what honesty can enforce. [https://eips.ethereum.org/EIPS/eip-8369]

Below the table, the exception would still have practical force. A committee could receive an excluded transaction and carry it on a list. Under Thiery’s reference model, that same committee would still lack the power to compel its inclusion. [https://eips.ethereum.org/EIPS/eip-8369]

SOURCES

Thomas Thiery, EIP-8369: VOPS Profiles for FOCIL Eligibility. Draft Informational reference model; profiles, exclusions, insertion indices, budgets and integration requirements. [https://eips.ethereum.org/EIPS/eip-8369]

Thomas Thiery and co-authors, EIP-7805: Fork-choice enforced Inclusion Lists. Draft committee, omission and voting rules, with their builder-work rationale. [https://eips.ethereum.org/EIPS/eip-7805]

Ethereum.org, Hegotá roadmap. Page updated 16 October 2026; scheduled changes, planning status and supporting proposals under consideration. [https://ethereum.org/roadmap/hegota/]

Ethereum Foundation Protocol Cluster, EF Protocol: Current and Emerging Priorities, 7 September 2026. Implementation expectations and the requirement for joint inclusion-list and frame testing. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

Vitalik Buterin and co-authors, EIP-8141: Frame Transaction. Validation prefixes, payment, execution and public-mempool policy. [https://eips.ethereum.org/EIPS/eip-8141]

Thomas Thiery and co-authors, EIP-8272: Recent Roots for Frame Transactions. Root verification, publication, reference lifetime and application responsibilities. [https://eips.ethereum.org/EIPS/eip-8272]

Thomas Thiery and co-authors, EIP-8250: Keyed Nonces for Frame Transactions. Replay domains and the retained public-pool limit. [https://eips.ethereum.org/EIPS/eip-8250]

METHOD

Drafts B (drafts/b.md) and C (drafts/c.md) carry the opening, inclusion-list explanation, wallet-storage analysis, claimed-index section and cost argument; draft A (drafts/a.md) adds privacy mechanics and the closing integration caveat. Drafts A and B carry the privacy section; the edit cuts A’s nonce-encoding comparison, detailed debit mechanics and B’s hypothetical third profile. The rewrite adds no reporting, uses no secondary sources or interviews, and follows the house feature register; prospective consequences remain inferences, while document differences establish no deployed failure. [https://raw.githubusercontent.com/openinterest-ai/paper/main/style-guide.html]

Ethereum’s proposed censorship guarantee has an eligibility test.

STANDFIRST

Ethereum’s proposed inclusion lists would constrain builders, but Thomas Thiery’s draft eligibility rules leave some transactions beyond enforcement. Wallet design could therefore determine access to that protection, an inference from the specification rather than evidence of censorship in operation. The boundary matters most where programmable accounts and privacy applications need the network to check more than a signature. [https://eips.ethereum.org/EIPS/eip-8369]

The exception in Thiery’s table

Thomas Thiery puts the dividing line in a table. The Ethereum proposal author assigns familiar transaction formats to one profile and programmable frame transactions to another. Below the table, his draft excludes ordinary privacy-contract storage, commitment trees and arbitrary external storage from the permitted validation data. [https://eips.ethereum.org/EIPS/eip-8369]

The document is EIP-8369, created on 5 August 2026. Its subject is eligibility for fork-choice enforced inclusion lists, abbreviated FOCIL: a proposed means of making validators constrain block builders. Thiery’s table describes which transactions a future extension could protect, rather than changing Ethereum’s rules itself. [https://eips.ethereum.org/EIPS/eip-8369]

The promise being qualified is substantial. EIP-7805 proposes committees whose members circulate transaction lists; validators checking the next block would withhold votes when its omissions breach the inclusion rules. A builder’s preference would no longer settle whether a listed transaction enters the chain. [https://eips.ethereum.org/EIPS/eip-7805]

That promise has particular force for programmable accounts. Ethereum.org describes proposed frame transactions as supporting account-defined verification, including multiple approvals, spending limits and payment of fees by another party. Those freedoms would let wallet designers choose more of the conditions under which an account acts. [https://ethereum.org/roadmap/hegota/]

Thiery’s document puts a condition on protection for that freedom. A frame transaction must use an accepted validation structure and stay within specified data and computation limits. Builders could still include transactions outside the profiles, but omission would carry no FOCIL enforcement under this model. [https://eips.ethereum.org/EIPS/eip-8369]

The feature’s argument follows from that distinction. If a wallet’s authorization checks need excluded storage, an honest committee member cannot turn its transaction into an enforceable claim merely by listing it. The exclusion concerns how the wallet establishes permission to act, rather than whether its intended action deserves approval. [https://eips.ethereum.org/EIPS/eip-8369]

This is a proposed boundary, not a finding that wallets have already suffered exclusion under deployed rules. EIP-8369 labels itself a draft Informational document and requires a future Standards Track extension to specify binding rules. Which applications would qualify cannot be settled before the enforcement parameters and implementations exist. [https://eips.ethereum.org/EIPS/eip-8369]

The timing gives the boundary practical importance. Ethereum.org’s Hegotá page, updated on 16 October 2026, schedules FOCIL and frame transactions while leaving supporting proposals under consideration. It lists recent roots and keyed nonces among candidates whose consideration does not establish that they will ship. [https://ethereum.org/roadmap/hegota/]

The Ethereum Foundation’s Protocol cluster addressed their interaction on 7 September 2026. It placed possible implementation work in late 2026 and said inclusion lists and frames must undergo testing together. The upgrade’s promise therefore meets its eligibility question in the same engineering programme. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

A list is a conditional claim

EIP-7805 divides responsibility among committee members, builders and attesters. Committee members select transactions; builders construct blocks; attesters cast the votes that enforce compliance. The committee supplies a constraint, while the attesters decide whether a particular block satisfies it. [https://eips.ethereum.org/EIPS/eip-7805]

The distinction matters because a list cannot make an invalid transaction valid. EIP-7805 allows omission when the listed transaction would be invalid after the block’s transactions execute. It also allows omission when the transaction’s gas requirement exceeds the block’s remaining gas. [https://eips.ethereum.org/EIPS/eip-7805]

Gas measures computational work and limits how much a block can contain. Under the proposed check, attesters examine the omitted transaction against the completed block’s resulting state. A sufficient balance and appropriate nonce are among the conditions that determine whether its absence is justified. [https://eips.ethereum.org/EIPS/eip-7805]

A nonce is an account counter used to distinguish successive transactions. Another transaction can change that counter or spend the account’s available balance before the final check. The inclusion rule consequently makes a conditional demand on builders, rather than reserving unconditional execution for every listed item. [https://eips.ethereum.org/EIPS/eip-7805]

Nor does the committee promise to select every pending transaction. EIP-7805 leaves list-building strategies to implementers, including selection by fees, waiting time or random choice. Its proposed committee has 16 members, each with an 8 KiB list limit, rather than unlimited capacity to nominate transactions. [https://eips.ethereum.org/EIPS/eip-7805]

Those limits separate the opportunity to be nominated from the enforcement that follows nomination. Even an eligible transaction needs an includer to receive it and put it on a usable list. Thiery expressly states that enforcement cannot operate when no includer sees the transaction. [https://eips.ethereum.org/EIPS/eip-8369]

A further separation concerns the public mempool, the pool of pending transactions that nodes accept and relay. EIP-8369 treats admission there and eligibility for inclusion enforcement as independent checks. A transaction can satisfy either, both or neither. [https://eips.ethereum.org/EIPS/eip-8369]

This cuts in both directions. A frame transaction admitted to the public pool might fail the narrower storage requirements for enforcement. Conversely, Thiery’s enforcement model permits certain payer-storage reads that public-pool policy would not accept, potentially requiring direct submission or a custom pool. [https://eips.ethereum.org/EIPS/eip-8369]

The route changes who encounters a transaction; it does not rewrite the eligibility test. An includer can receive an eligible transaction directly without the public pool’s blessing. A public-pool acceptance message, equally, cannot establish that omission would cost a builder the attesters’ votes. [https://eips.ethereum.org/EIPS/eip-8369]

The resulting distinction is useful for interpreting a wallet’s promise to submit a transaction. Submission, circulation, nomination and enforceability are separate stages under the proposed rules. A transaction can make progress through the first stages and still reach an exception at the last. [https://eips.ethereum.org/EIPS/eip-8369]

The wallet’s storage becomes part of the promise

Thiery’s first profile covers legacy transactions and the formats specified by EIP-2930, EIP-1559 and EIP-7702. The model checks their validity using a limited account record, without executing sender code for eligibility. These transactions retain the end-of-block omission test. [https://eips.ethereum.org/EIPS/eip-8369]

The underlying method is validity-only partial statelessness, or VOPS. In this model, nodes retain selected account information needed for validity checks rather than the entire application state for those checks. The first profile relies on nonce, balance and a classification of account code. [https://eips.ethereum.org/EIPS/eip-8369]

The second profile addresses EIP-8141 frame transactions, whose validation is programmable. A frame is a component of a transaction with a specified role, such as verification or payment. Programmable validation can consult more information than the first profile’s account record supplies. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery expands the retained information but draws a perimeter around it. Nodes would hold code, keyed nonce state, recent roots and a limited range of account storage. For a particular transaction, permitted storage reads include the designated initial slots of its sender and payer. [https://eips.ethereum.org/EIPS/eip-8369]

The slot count remains unresolved. EIP-8369 gives a candidate range of two to four initial slots per account, subject to benchmarks and selection by the enforcing proposal. Those few locations contrast with arbitrary storage addresses, which the profile excludes. [https://eips.ethereum.org/EIPS/eip-8369]

The practical consequence is an inference about design. Two wallets could offer similar approval policies while storing the information those policies need in different locations. Under Thiery’s model, their transactions could receive different enforcement treatment because validation reads different data. [https://eips.ethereum.org/EIPS/eip-8369]

The draft makes that possibility concrete by excluding mappings, proxy slots and namespaced storage at hash-derived locations from the permitted reads. It also requires accepted validation-prefix shapes and successful payment authorization. Fitting into the storage perimeter is necessary, but does not alone establish eligibility. [https://eips.ethereum.org/EIPS/eip-8369]

This boundary applies to validation, the checks establishing whether the transaction may proceed. The document does not impose the same small storage perimeter on every later application action. Treating the rule as a ban on all complex contract execution would misidentify what the profiles regulate. [https://eips.ethereum.org/EIPS/eip-8369]

Code sharing also remains possible. The second profile permits authenticated code reached during validation, including shared verifier contracts, while keeping storage reads restricted. The dividing line therefore does not simply separate wallets that call other contracts from wallets that operate alone. [https://eips.ethereum.org/EIPS/eip-8369]

There is another categorical exclusion: transactions carrying blobs. Thiery explains that blob gas has a separate target and maximum, and the model supplies no omission test for that second budget. Both blob transactions and blob-carrying frame transactions fall outside the two profiles. [https://eips.ethereum.org/EIPS/eip-8369]

These are technical eligibility conditions rather than judgments about an application’s purpose. Nevertheless, their effect would reach the person authorizing a payment through a wallet. The inference is that a wallet’s internal validation design could determine which network promise accompanies that authorization. [https://eips.ethereum.org/EIPS/eip-8369]

A privacy spend gets a narrow bridge

Privacy transactions supply Thiery’s motivating example for the second profile. The draft describes a spend using recent roots and consuming a single-use keyed nonce. It expressly excludes reading ordinary commitment trees or nullifier mappings as part of the profile’s validation. [https://eips.ethereum.org/EIPS/eip-8369]

A root is a compact commitment to an application’s data. EIP-8272, co-authored by Thiery, describes privacy applications that prove spending rights against a recent commitment-tree root. The proposed mechanism makes that recent commitment available through a standard verification frame. [https://eips.ethereum.org/EIPS/eip-8272]

The distinction is between consulting a whole application’s mutable storage and checking a declared recent commitment. Under EIP-8272, the transaction supplies a source identifier, a slot and a root. A designated contract checks those references against stored entries before account validation in the public-pool sequence. [https://eips.ethereum.org/EIPS/eip-8272]

The contract does not decide what the commitment means. Applications remain responsible for identifying the expected source and binding the reference to the statement being authorized. A successful recent-root check establishes storage and recency, rather than the truth of every application claim attached to the root. [https://eips.ethereum.org/EIPS/eip-8272]

The proposal allows up to 16 references in that verifier frame. Its storage ring has 8,192 positions per source, with references usable for up to 8,191 slots. The difference excludes the current slot, whose writes are still taking place. [https://eips.ethereum.org/EIPS/eip-8272]

That timing provides the important property. A source can write a root during one slot, but transactions may reference it only from the following slot. Current-slot writes therefore cannot overwrite an entry that remains valid within the usable reference window. [https://eips.ethereum.org/EIPS/eip-8272]

This is a designed form of stability, not a declaration that application state never changes. A chain reorganization can remove an entry, and a reference can expire as slots advance. EIP-8272 requires clients to track dependencies and recheck affected transactions when those conditions change. [https://eips.ethereum.org/EIPS/eip-8272]

The privacy spend also needs protection against reuse. EIP-8369’s example treats each nullifier, a single-use marker preventing another spend of the same right, as a keyed nonce. Its security conditions require the proof to authenticate the relevant nonce keys, roots, domain, execution and payment intent. [https://eips.ethereum.org/EIPS/eip-8369]

The architecture suggests a route into enforceability for some privacy designs. Application commitments become recent-root references; single-use spending markers become protocol-managed nonce checks. That is an inference about the proposed mechanism, not a finding that an existing privacy application already satisfies it. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272]

There is a missing guarantee underneath that route. EIP-8272 does not ensure that the transaction publishing a root gets included. Its security discussion says applications needing timely publication must arrange a publication path, redundant sources or an inclusion policy for those writes. [https://eips.ethereum.org/EIPS/eip-8272]

A protected spend would thus depend on a commitment that first has to reach the chain. The recent-root mechanism makes a published commitment checkable; it does not make publication inevitable. The application’s route to protection begins before the person asks the wallet to spend. [https://eips.ethereum.org/EIPS/eip-8272]

The builder still chooses a position

Thiery’s second profile contains a qualification beyond the admission boundary. For an omitted frame transaction, a builder may claim an insertion index anywhere from before the first transaction to after the last. Attesters would test the omission at that claimed position. [https://eips.ethereum.org/EIPS/eip-8369]

They would reconstruct the relevant account state from the parent block and changes preceding the selected index. They would then replay validation and check fees, budget admission and remaining gas there. The builder’s claimed index is not evidence that insertion was actually attempted. [https://eips.ethereum.org/EIPS/eip-8369]

This creates a weaker guarantee for transactions whose validity changes with position. Thiery’s security discussion states that protection requires validity at every index the builder could claim. A position where validation fails can justify omission even when validation succeeds elsewhere in the block. [https://eips.ethereum.org/EIPS/eip-8369]

The draft supplies a concrete case: a transaction waiting for a nonce predecessor in the same block. It can be invalid before that predecessor executes and valid afterward. The builder can claim the earlier index, so the later opportunity to execute does not itself establish unjustified omission. [https://eips.ethereum.org/EIPS/eip-8369]

Payment introduces another dependency. When several transactions share a payer, another sponsored transaction can reduce that payer’s balance before the claimed index. Thiery says payment capacity qualifies for the stronger property only when it is reserved for the transaction. [https://eips.ethereum.org/EIPS/eip-8369]

The same concern reaches authorization storage. A validation slot provides the needed stability only if another authorized transaction cannot change it. A wallet’s use of the permitted slots therefore does not, by itself, remove every opportunity for position-dependent invalidity. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery calls the relevant property position stability. A dependency qualifies when it stays constant within the block or changes so that invalidity persists through the block’s end. Recent roots and fresh single-use keyed nonces supply examples in the draft. [https://eips.ethereum.org/EIPS/eip-8369]

That is why the privacy example and the index rule belong in the same account. Recent roots do more than provide another readable value: their timing helps preserve validation conditions across positions. A feature that counted eligible formats without examining those conditions would overstate the protection. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272]

Thiery also closes a different escape route. An attester lacking required state or matching code cannot treat its own missing data as justification for omission. It must obtain authenticated information or synchronize before evaluating the transaction. [https://eips.ethereum.org/EIPS/eip-8369]

The trade is consequently specific. Builders gain discretion over the state at which an omitted frame transaction is tested; attesters still need the data to test it correctly. For wallets, reaching the permitted profile and remaining valid across positions would be distinct design problems. [https://eips.ethereum.org/EIPS/eip-8369]

The limit pays for the guarantee

The strongest objection to the feature’s thesis comes from Thiery’s own rationale. Enforceable inclusion asks validators to do extra work even when a listed transaction never executes. An unrestricted validation programme could make checking omissions expensive enough to threaten the mechanism intended to resist censorship. [https://eips.ethereum.org/EIPS/eip-8369]

Omitted transactions pay no fees, the security discussion notes. Their checks therefore need limits before adoption, including benchmarks against the attestation deadline. The profile boundary is a defence against unpaid verification work, rather than an unexplained preference for simpler wallets. [https://eips.ethereum.org/EIPS/eip-8369]

The draft proposes roughly 1.05 million verification gas per inclusion list as a candidate cap. Across 16 includers, that implies roughly 16.8 million metered verification gas per slot. Those are proposed workload bounds pending benchmarks, not measurements of deployed performance. [https://eips.ethereum.org/EIPS/eip-8369]

The limits would count declared validation work, including signature costs and optional expiry checks. A separate per-transaction ceiling could permit one transaction to consume an entire list’s verification budget or divide capacity among several. Passing the storage test would not override those limits. [https://eips.ethereum.org/EIPS/eip-8369]

Even gas caps do not finish the calculation. Thiery notes that metered gas does not directly bound all bytes loaded from distinct code bodies. The enforcing proposal would also need code-count and byte limits, plus benchmarks covering state reconstruction and replay together. [https://eips.ethereum.org/EIPS/eip-8369]

The index mechanism serves the same cost argument. Testing omissions at one claimed position avoids an earlier repeated-append approach that could require quadratic work. Thiery accepts weaker protection for position-dependent transactions in exchange for a tractable check. [https://eips.ethereum.org/EIPS/eip-8369]

A hypothetical third profile might admit external storage through witnesses or proofs. The draft postpones it because commitments, freshness, size limits and omission rules remain necessary. Evidence for broader eligibility is therefore a research agenda, not an available remedy for an excluded wallet. [https://eips.ethereum.org/EIPS/eip-8369]

This objection narrows the verdict. The documents do not establish that unlimited enforcement would be safe, or that the proposed limits exclude more applications than necessary. They establish that affordable verification and broad programmability require an explicit compromise. [https://eips.ethereum.org/EIPS/eip-8369]

There are unresolved integration conditions as well. EIP-8369 requires activated frame, keyed-nonce and recent-root support, authenticated state changes, an index encoding and conformance tests. Under enshrined proposer-builder separation, it also requires omission checks after payload revelation or leaves the second profile disabled. [https://eips.ethereum.org/EIPS/eip-8369]

The Protocol cluster’s September priorities describe these components as connected commitments to censorship resistance and privacy. The same post makes safe joint testing of FOCIL and frames the central engineering task. That endorsement supplies direction; it does not supply the missing benchmark results. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

No interview evidence in this feature establishes how wallet teams would change their designs or what those changes would cost. The specification itself supplies the criticism’s strongest answer: the perimeter makes enforcement reproducible and bounded. Its consequences for particular products need implementation evidence beyond this document record. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery’s table remains the place where the promise changes shape. Under its proposed rules, an includer could receive a transaction, recognize the intended action and place it on a list. If its validation crosses the eligibility boundary, the builder could still leave it out without an enforceable omission. [https://eips.ethereum.org/EIPS/eip-8369]

SOURCES

Thomas Thiery, EIP-8369: VOPS Profiles for FOCIL Eligibility. Draft Informational proposal; eligibility profiles, index checks, budgets, exclusions and integration requirements. [https://eips.ethereum.org/EIPS/eip-8369]

Thomas Thiery and co-authors, EIP-7805: Fork-choice enforced Inclusion Lists. Draft Core proposal; committee duties, conditional inclusion and attester checks. [https://eips.ethereum.org/EIPS/eip-7805]

Thomas Thiery, Vitalik Buterin, Toni Wahrstätter and lightclient, EIP-8272: Recent Roots for Frame Transactions. Draft Core proposal; root publication, verification, expiry and application responsibilities. [https://eips.ethereum.org/EIPS/eip-8272]

Ethereum.org, Hegotá roadmap. Page dated 16 October 2026; scheduled changes and supporting proposals under consideration. [https://ethereum.org/roadmap/hegota/]

Ethereum Foundation Protocol Cluster, EF Protocol: Current and Emerging Priorities, 7 September 2026. Engineering priorities and the interaction between inclusion lists and frame transactions. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

METHOD

The reporting swept the five listed primary documents on 7 November 2026 and checked the Open Interest feature register. Broader upgrade subjects, market claims and application rankings were cut; no secondary reporting or interviews supplied evidence. Wallet consequences are labeled inferences; no client benchmark, live enforcement result or product compatibility claim is asserted. [https://raw.githubusercontent.com/openinterest-ai/paper/main/style-guide.html] [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-7805] [https://eips.ethereum.org/EIPS/eip-8272] [https://ethereum.org/roadmap/hegota/] [https://blog.ethereum.org/2026/09/07/protocol-priorities]

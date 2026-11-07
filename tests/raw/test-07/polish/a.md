HEADLINE

Ethereum’s proposed censorship guarantee has an eligibility test

STANDFIRST

Ethereum’s proposed inclusion lists would constrain block builders, but Thomas Thiery’s eligibility draft would leave some listed transactions outside that protection. Wallet validation and payment design could therefore help determine which refusals carry a protocol consequence. That is an inference from proposed rules, not evidence of censorship in operation. [https://eips.ethereum.org/EIPS/eip-8369]

## The exception in Thiery’s table

Thomas Thiery puts the dividing line in a table. One row covers familiar transaction formats; another covers programmable validation. Below them, his Ethereum proposal identifies transactions that would receive no enforced inclusion. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery also helped write the inclusion-list proposal whose protection this later document qualifies. That proposal would give validators a way to constrain which transactions builders leave out. The same author appears beside both the promise and its boundary. [https://eips.ethereum.org/EIPS/eip-7805] [https://eips.ethereum.org/EIPS/eip-8369]

The promise concerns an ordinary act: getting a submitted transaction into a block despite its assembler’s preferences. Builders choose the transactions that make up blocks. EIP-7805 would let validator committees circulate lists whose unjustified omissions could cause other validators to withhold their votes. [https://eips.ethereum.org/EIPS/eip-7805]

Its authors attribute the need to concentrated block production and deteriorating censorship resistance. That is their diagnosis, rather than an independently measured finding here. Their remedy would give transactions a route beyond voluntary builder selection, making some refusals consequential under the protocol. [https://eips.ethereum.org/EIPS/eip-7805]

Another proposed change would give accounts more freedom over what they authorize. Ethereum.org describes frame transactions as supporting account-defined verification, including multiple approvals, recovery arrangements and payment of fees by another party. Those freedoms put more of an account’s operating conditions in wallet designers’ hands. [https://ethereum.org/roadmap/hegota/]

The two proposals meet at validation: the checks establishing whether a transaction may proceed. A programmable account can require more than a fixed signature check. Enforcing its inclusion would require other participants to reproduce the relevant checks within bounded resources. [https://eips.ethereum.org/EIPS/eip-8141] [https://eips.ethereum.org/EIPS/eip-8369]

Thiery’s EIP-8369, created on 5 August 2026, describes that boundary. It is a draft Informational reference model, requiring a future Standards Track extension to establish binding enforcement. Its existence changes no Ethereum rule. [https://eips.ethereum.org/EIPS/eip-8369]

The engineering work nevertheless has a proposed destination. Ethereum.org’s Hegotá roadmap, updated on 16 October 2026, schedules inclusion lists and frame transactions. It describes an upgrade in planning, with an unconfirmed mainnet expectation of April–June 2027. [https://ethereum.org/roadmap/hegota/]

The Ethereum Foundation’s Protocol cluster addressed their interaction on 7 September 2026. Its priorities document placed possible implementation work in late 2026 and required inclusion lists and frames to undergo testing together. That implementation prospect is distinct from activation on mainnet. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

The inference from Thiery’s model is narrower than a verdict on Ethereum’s censorship resistance. A wallet could create a transaction that a willing builder can execute, while failing to create an enforceable demand for inclusion. The freedom to define authorization would not automatically bring protection for every way of defining it. [https://eips.ethereum.org/EIPS/eip-8369]

## What a list can demand

EIP-7805 calls its mechanism fork-choice enforced inclusion lists, abbreviated FOCIL. Fork choice determines which chain validators support. Under the proposal, their votes would depend on whether blocks satisfy the lists they stored. [https://eips.ethereum.org/EIPS/eip-7805]

The proposed committee has 16 validators, each able to contribute a list capped at 8 KiB of encoded transactions. This distributes nomination across committee members rather than leaving selection entirely to a builder. It does not provide unlimited nomination space. [https://eips.ethereum.org/EIPS/eip-7805]

Implementers retain discretion over list construction, including selection by fees, waiting time or random choice. Builders collect lists, while attesters, the validators voting on blocks, check compliance. Eligibility alone therefore would not ensure that a particular transaction gets nominated. [https://eips.ethereum.org/EIPS/eip-7805]

Nomination would not guarantee execution either. EIP-7805 permits omission when a transaction would be invalid after the block’s other transactions execute. It also permits omission when the remaining block gas cannot accommodate the transaction’s declared requirement. [https://eips.ethereum.org/EIPS/eip-7805]

Gas measures and limits execution resources. For familiar transaction formats, validity checks principally concern the sender’s balance and nonce, an account counter distinguishing successive transactions. Other transactions can spend the funds or advance the counter before the final check. [https://eips.ethereum.org/EIPS/eip-7805]

Thiery’s eligibility model adds a separate condition: the transaction must fit a supported profile. Transactions outside both profiles may still reach inclusion lists, but their omission is excused. A committee member’s willingness to nominate would not remove that exception. [https://eips.ethereum.org/EIPS/eip-8369]

The model also separates enforcement eligibility from admission to the public mempool, the pool of pending transactions nodes accept and relay. A transaction may pass either check, both or neither. Public circulation would not certify an enforceable claim. [https://eips.ethereum.org/EIPS/eip-8369]

Conversely, an eligible transaction could reach an includer through direct submission or a custom pool. Thiery’s model permits certain payer-storage reads that public-pool policy would reject. Such a transaction could need another distribution route without losing eligibility on that ground. [https://eips.ethereum.org/EIPS/eip-8369]

The route still needs a recipient. Thiery warns that FOCIL cannot enforce a transaction no includer has received, and identifies denial-of-service, metadata and private-access-market risks around direct endpoints. Those risks remain implementation questions rather than observations of deployed enforcement. [https://eips.ethereum.org/EIPS/eip-8369]

The inferred consequence for a wallet’s submission message is concrete. Delivery, circulation, nomination and enforceability would describe separate conditions. A transaction could reach willing intermediaries and still lack a protocol remedy against an unwilling builder. [https://eips.ethereum.org/EIPS/eip-8369]

## The wallet carries the boundary

Thiery organizes eligibility around validity-only partial statelessness, or VOPS. The approach retains selected information needed to check validity rather than making all application state available for those checks. Its two profiles accommodate different validation requirements. [https://eips.ethereum.org/EIPS/eip-8369]

The first covers legacy transactions and the formats specified by EIP-2930, EIP-1559 and EIP-7702. It retains the end-of-block omission check, including sender, fee and remaining-gas conditions. Eligibility classifies the sender’s code without executing it. [https://eips.ethereum.org/EIPS/eip-8369]

Empty-code accounts and permitted delegated accounts can originate transactions within this profile’s conditions. The boundary therefore does not simply divide accounts with code from accounts without it. Some programmable arrangements already sit within the familiar-format profile. [https://eips.ethereum.org/EIPS/eip-8369]

The second profile covers certain frame transactions. Frames are contract calls separating verification, payment approval and subsequent application operations within a transaction. Account abstraction lets account code define authorization and payment instead of relying exclusively on a fixed signature rule. [https://eips.ethereum.org/EIPS/eip-8141]

For those preliminary checks, Thiery permits specified account fields, authenticated code, keyed nonce state and recent roots. He also permits a small initial range of storage slots belonging to the sender and payer. A storage slot is an indexed location holding contract state. [https://eips.ethereum.org/EIPS/eip-8369]

The candidate range starts at slot zero and contains two to four initial slots per account. That range contrasts with permission to read arbitrary storage elsewhere. Its final size awaits benchmarks and a binding choice in the enforcing proposal; Profile 2 cannot be classified for enforcement before that choice. [https://eips.ethereum.org/EIPS/eip-8369]

The draft excludes arbitrary external storage and ordinary privacy-contract mappings from validation. Proxy slots and namespaced storage at derived locations also fall outside the permitted range. A small amount of information in an excluded location would still be excluded. [https://eips.ethereum.org/EIPS/eip-8369]

The resulting wallet comparison is an inference, not a compatibility test. Similar approval functions could consult different storage and receive different enforcement treatment. No named wallet has been tested here, and the documents provide no application compatibility census. [https://eips.ethereum.org/EIPS/eip-8369]

The restriction concerns the validation prefix, the preliminary frames ending when a payer is established. It does not impose the same storage perimeter on every subsequent application operation. Complex application execution therefore does not automatically make a transaction ineligible. [https://eips.ethereum.org/EIPS/eip-8141] [https://eips.ethereum.org/EIPS/eip-8369]

Nor does calling another contract automatically create an exclusion. Profile 2 permits authenticated code reached during validation, including shared verifier contracts, while restricting the state those checks can read. The verifier’s dependencies matter alongside its existence. [https://eips.ethereum.org/EIPS/eip-8369]

Transaction structure matters too: the draft requires accepted validation patterns and payment authorization. Blob transactions, including frame transactions carrying blobs, fall outside both profiles because the model supplies no omission check for the separate blob-gas budget. These exclusions concern enforcement, not a ban on voluntary inclusion. [https://eips.ethereum.org/EIPS/eip-8369]

For the person authorizing a payment, the inferred consequence sits behind the wallet’s visible function. How its code establishes permission could determine which network protection accompanies the transaction. A builder could accept the action while retaining the right to refuse it under this model. [https://eips.ethereum.org/EIPS/eip-8369]

## The builder chooses the testing point

Even an eligible frame transaction faces another qualification. Profile 2 permits a builder to claim an insertion index, identifying where in the block validators should evaluate an omitted transaction. The position can precede the first transaction, fall between transactions or follow the last. [https://eips.ethereum.org/EIPS/eip-8369]

Attesters would reconstruct the state at that position and replay validation. They would check eligibility, fees, list-budget admission and remaining gas there. A missing, malformed or out-of-range index defaults to the block’s end. [https://eips.ethereum.org/EIPS/eip-8369]

The claimed index would not prove that the builder attempted insertion. Thiery’s security discussion states the consequence: protection requires validity at every index the builder could claim. A transaction valid somewhere in the block could still have an omission justified elsewhere. [https://eips.ethereum.org/EIPS/eip-8369]

The draft’s sequencing example makes the distinction tangible. A queued transaction might require a predecessor to advance the sender’s nonce in the same block. It can be invalid before that predecessor and valid afterward, leaving the earlier position available to justify omission. [https://eips.ethereum.org/EIPS/eip-8369]

Fee sponsorship introduces a similar dependency. Another sponsored transaction could reduce a shared payer’s balance before the chosen index. Thiery identifies weaker protection where that payer has not reserved payment capacity for the transaction. [https://eips.ethereum.org/EIPS/eip-8369]

For a person using a sponsored wallet, the inferred difference would depend on the payment arrangement. Offering sponsorship alone would not establish equivalent protection for every payment. Another transaction’s ability to consume the same funds could matter at the moment validators test the omission. [https://eips.ethereum.org/EIPS/eip-8369]

Thiery contrasts these cases with dependencies he calls position-stable. They remain constant within the block, or change so that invalidity at an earlier point persists through its end. For such transactions, the claimed-index guarantee matches the original end-of-block rule. [https://eips.ethereum.org/EIPS/eip-8369]

Recent roots and fresh single-use keyed nonces supply examples. Validation storage qualifies only when another authorized transaction cannot change it; payment capacity qualifies only when reserved. Stability is a property of the dependencies, rather than a benefit conferred by calling an account a smart wallet. [https://eips.ethereum.org/EIPS/eip-8369]

These examples describe permitted outcomes under draft rules, not observed builder tactics. They also establish two distinct limits. Reading excluded storage can remove enforcement entirely; changing permitted state can weaken protection for a transaction that remains within the profile. [https://eips.ethereum.org/EIPS/eip-8369]

## Privacy needs an earlier transaction

Privacy transactions are a motivating case for Profile 2. Thiery describes a spend checking recent roots and consuming single-use keyed nonces, without reading unrestricted privacy-contract storage during validation. The proposed route translates application dependencies into information the profile permits. [https://eips.ethereum.org/EIPS/eip-8369]

A root is a compact commitment to a larger body of application data. EIP-8272, co-authored by Thiery, describes privacy applications proving spends against recent commitment-tree roots. Its standard verification frame would check recorded commitments before account validation. [https://eips.ethereum.org/EIPS/eip-8272]

The transaction identifies references by source, slot and root; a designated contract checks them against stored entries. Successful verification establishes that the specified reference is stored and recent. Applications remain responsible for what the commitment means and for binding it to the authorized action. [https://eips.ethereum.org/EIPS/eip-8272]

The timing supplies a useful form of stability. A root written during one slot becomes referenceable from the following slot, rather than while that slot’s writes are changing. Each source has 8,192 storage positions, with 8,191 prior slots usable because the current slot is excluded. [https://eips.ethereum.org/EIPS/eip-8272]

Current-slot writes cannot overwrite references still within the usable window. A chain reorganization can nevertheless remove an entry, and references expire as slots advance. Clients must track dependencies and recheck affected transactions. [https://eips.ethereum.org/EIPS/eip-8272]

Keyed nonces address a different dependency: users sharing a sender without sharing one mandatory sequence. A nonce key selects an independent replay-protection domain. Disjoint key sets can avoid invalidating each other through a shared counter, including keys derived from single-use privacy-spend markers called nullifiers. [https://eips.ethereum.org/EIPS/eip-8250]

That capability does not establish unrestricted public-pool concurrency. EIP-8250 preserves the one-pending-frame-transaction-per-sender public-mempool limit. As with enforcement eligibility, what the transaction can express and how it can circulate remain separate questions. [https://eips.ethereum.org/EIPS/eip-8250]

The privacy proof still must authenticate what the spend authorizes. Thiery’s security conditions include the sender, nonce keys, precise root references, chain and contract domain, and intended execution and payment. An eligible path would not replace those application responsibilities. [https://eips.ethereum.org/EIPS/eip-8369]

The documents also leave a composition question. EIP-8272 explicitly skips its leading root-verification frame when matching validation patterns; EIP-8369’s pattern rule explicitly skips only an optional expiry frame. EIP-8369 requires a composed encoding and signature hash before activation. [https://eips.ethereum.org/EIPS/eip-8272] [https://eips.ethereum.org/EIPS/eip-8369]

The inference is that combining these documents does not yet establish a finished enforcement implementation. That is not evidence that the approach cannot work. It limits what the written proposals establish about a privacy wallet’s eventual protection. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-8272]

A more basic dependency comes first: the root must reach the chain. EIP-8272 guarantees no inclusion for root-writing transactions, leaving timely publication paths to applications. A spend’s checkable commitment would depend on an earlier transaction whose publication the root mechanism does not compel. [https://eips.ethereum.org/EIPS/eip-8272]

## The work behind the promise

Thiery supplies the strongest answer to criticism of the boundary. Enforceable inclusion requires extra verification even when a listed transaction never executes. His draft states: “Profile 2 trades guarantee strength for replay cost.” [https://eips.ethereum.org/EIPS/eip-8369]

The index method avoids an earlier repeated-check approach that could require quadratic builder work. Checking effort could grow much faster than the number of candidate transactions. EIP-7805 illustrates the problem with transactions successively funding one another and repeatedly changing which pending transactions become valid. [https://eips.ethereum.org/EIPS/eip-8369] [https://eips.ethereum.org/EIPS/eip-7805]

Profile 2 proposes roughly 1.05 million verification gas per list. Across 16 includers, that implies roughly 16.8 million metered verification gas per slot. Both are candidate workload limits awaiting benchmarks, rather than measurements of deployed performance. [https://eips.ethereum.org/EIPS/eip-8369]

The accounting uses declared validation limits plus signature costs, rather than anticipated cheap execution. Transactions consume allowance in list order before duplicate removal. Enforcement needs at least one occurrence admitted under that procedure, alongside successful state-dependent checks. [https://eips.ethereum.org/EIPS/eip-8369]

Even this arithmetic does not establish the whole burden. Metered gas does not directly bound every byte loaded from distinct code bodies. Omitted transactions pay no fees, while attesters still need to reconstruct state and replay validation within their deadline. [https://eips.ethereum.org/EIPS/eip-8369]

Restricting categories of retained state also does not cap their aggregate volume. Code, keyed nonce entries, recent-root sources and low-numbered account storage can grow. The draft calls for benchmarks and parameter choices covering storage growth as well as checking time. [https://eips.ethereum.org/EIPS/eip-8369]

The objection therefore narrows the argument about wallet freedom. The documents do not establish that unrestricted enforcement would be safe, or that these particular limits exclude more applications than necessary. They establish a compromise between broad programmability and reproducible, bounded verification. [https://eips.ethereum.org/EIPS/eip-8369]

Consensus integration presents another unfinished condition. Under the proposer-builder separation described in EIP-8369, payloads become available after beacon attestations. The enforcing extension would need an omission-checking duty after revelation, or leave Profile 2 disabled in that setting. [https://eips.ethereum.org/EIPS/eip-8369]

The roadmap still places keyed nonces and recent roots under consideration; the Protocol cluster requires safe joint testing of frames and inclusion lists. Neither document supplies benchmark results or a catalogue of qualifying wallets. Direction and demonstrated performance remain different kinds of evidence. [https://ethereum.org/roadmap/hegota/] [https://blog.ethereum.org/2026/09/07/protocol-priorities]

No interviews or application tests supplement this document record. Missing evidence includes client benchmarks, named-wallet compatibility and what redesign would cost wallet teams. Thiery’s published rationale supplies the defence of the limits; no separate response to this feature was sought.

His table remains the place where the promise changes. An includer could receive a transaction and carry it on a list, while a willing builder could still execute it. Outside both profiles, that same list would give the committee no power under this model to compel inclusion. [https://eips.ethereum.org/EIPS/eip-8369]

SOURCES

Thomas Thiery, EIP-8369: VOPS Profiles for FOCIL Eligibility. Draft Informational reference model: profiles, exclusions, claimed indices, budgets and integration requirements. [https://eips.ethereum.org/EIPS/eip-8369]

Thomas Thiery and co-authors, EIP-7805: Fork-choice enforced Inclusion Lists. Draft committee, conditional inclusion and voting rules. [https://eips.ethereum.org/EIPS/eip-7805]

Vitalik Buterin and co-authors, EIP-8141: Frame Transaction. Validation prefixes, payment and application execution. [https://eips.ethereum.org/EIPS/eip-8141]

Thomas Thiery and co-authors, EIP-8272: Recent Roots for Frame Transactions. Publication, verification, reference lifetime and application responsibilities. [https://eips.ethereum.org/EIPS/eip-8272]

Thomas Thiery and co-authors, EIP-8250: Keyed Nonces for Frame Transactions. Replay-protection domains and retained public-pool limits. [https://eips.ethereum.org/EIPS/eip-8250]

Ethereum.org, Hegotá roadmap, updated 16 October 2026. Planned changes, unconfirmed activation expectation and supporting proposals under consideration. [https://ethereum.org/roadmap/hegota/]

Ethereum Foundation Protocol Cluster, EF Protocol: Current and Emerging Priorities, 7 September 2026. Implementation expectations and joint testing of frames and inclusion lists. [https://blog.ethereum.org/2026/09/07/protocol-priorities]

METHOD

This rewrite uses only material carried by drafts/a.md, drafts/b.md and drafts/c.md. Draft B carried the table opening, stakes, distribution distinctions and cost counterargument; draft C carried the builder-index examples and privacy composition question. Draft A carried the frame definitions, keyed-nonce explanation, benchmark limits and closing return to excluded transactions. The edit cut repeated eligibility warnings, detailed budget debits, the speculative third profile and surplus validation-pattern mechanics. All external evidence is attributed to the open primary documents already cited in those drafts; no secondary reporting, interviews, chain measurements or application tests were added. Wallet consequences remain labeled inferences, while draft status and missing implementation evidence limit the conclusions. The rewrite applied the house feature register. [https://raw.githubusercontent.com/openinterest-ai/paper/main/style-guide.html]

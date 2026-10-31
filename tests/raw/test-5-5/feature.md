HEADLINE

Ethereum is moving its receipts out of the room.

STANDFIRST

Ethereum’s execution clients can now discard much of the pre-Merge record while continuing to validate and follow the chain. The change makes running a current node cheaper, but it turns a familiar promise, that an old transaction can be fetched when needed, into a service supplied by archives, mirrors and a still-developing peer-to-peer network. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://eips.ethereum.org/EIPS/eip-4444]

THE RECEIPT IS THE ANSWER, NOT THE TRANSACTION.

An Ethereum transaction says what an account asked the network to do. A receipt records the result: whether the call succeeded, how much gas it used, and which logs it emitted. The execution API specification exposes that record through `eth_getTransactionReceipt`, including its status, gas fields, logs, block reference and transaction hash. [https://github.com/ethereum/execution-apis/blob/main/docs-api/api/methods/eth_getTransactionReceipt.mdx]

That distinction is more than database housekeeping. An application can have a transaction hash and still need the receipt to establish that a contract call completed, or to read the event it produced. Ethereum Foundation documentation lists proof that a transaction was sent, construction of chain indexes and validation of calldata-based layer-2 chains among the uses for old chain data. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

The word “onchain” has encouraged a useful but incomplete picture. It suggests that a public record is automatically close at hand. The protocol commits to a history through headers and hashes, but a person asking an ordinary node for an old body or receipt is asking for data that somebody must still retain and serve. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://eips.ethereum.org/EIPS/eip-4444]

This feature concerns access, not whether an old receipt becomes alterable. The Ethereum Foundation says execution clients continue to retain headers, allowing cryptographic checks of historical data against the chain, even as historical blocks move outside the ordinary peer-to-peer path. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

The practical question is therefore plain: who keeps the receipt long enough for a user, investigator, bridge operator or historian to ask for it? The answer used to be “nearly any fully synced node” for the old chain history. It is increasingly “whichever operator chose to keep it, or whichever distribution channel remains available.” [https://blog.ethereum.org/2025/07/08/partial-history-exp]

WHAT THE CLIENTS HAVE ACTUALLY CHANGED.

The first important correction is chronological. Ethereum’s EIP-4444 remains a draft networking standard, created on November 2, 2021, rather than a single completed consensus upgrade. Its text says clients should stop serving peer-to-peer headers, bodies and receipts older than 14,299 epochs, and may prune them locally. [https://eips.ethereum.org/EIPS/eip-4444]

The change already has a narrower, real form. On July 8, 2025, the Ethereum Foundation announced that all execution clients supported partial history expiry, meaning removal of data before the Merge rather than a rolling deletion of all old data. The announcement says the work on full rolling expiry was still ongoing. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

Geth, the Go Ethereum client, documents an offline `prune-history` command that removes historical block bodies and receipts up to the Merge block. Its documentation says the state trie and headers are preserved, and that the node remains functional for consensus after the operation. [https://geth.ethereum.org/docs/fundamentals/historypruning]

This is a consequentially boring command. It does not re-write a block, erase a header or revise a balance. It deletes a local copy of material the node no longer needs for its routine consensus role. [https://geth.ethereum.org/docs/fundamentals/historypruning] [https://blog.ethereum.org/2025/07/08/partial-history-exp]

The space is not trivial. The Foundation estimated that dropping pre-Merge block data could reduce a node’s disk requirement by 300 to 500 GB and let it fit comfortably on a 2 TB disk. Geth’s example at height 22,745,224 records 655.94 GiB of ancient bodies, 253.70 GiB of receipts, and 1.27 TiB in total. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://geth.ethereum.org/docs/fundamentals/historypruning]

Those figures describe different snapshots and tools, so they should not be added together or treated as a current network census. They establish the scale of the incentive: historical bodies and receipts occupy hundreds of gigabytes on a client that has kept them. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://geth.ethereum.org/docs/fundamentals/historypruning]

Home operators have received the message in plainer language. Eth Docker’s version 26.10.1 release, published on October 22, 2026, says its rolling-expiry notices had become more explicit about a retention period of about five months. That is a deployment tool’s warning, not an Ethereum protocol guarantee, but it shows how a proposed retention horizon reaches ordinary node administration. [https://github.com/ethstaker/eth-docker/releases/tag/v26.10.1]

THE CHEAPER NODE MAKES A DIFFERENT PROMISE.

There is a strong case for removing unused history from every machine. The EIP says historical blocks and receipts exceeded 400 GB when it was written, and that a typical validator then needed a 1 TB disk. It says those records are not needed to validate new blocks once a client has caught up. [https://eips.ethereum.org/EIPS/eip-4444]

The Foundation’s later account adds the proof-of-stake context. It says new clients anchor to a recent weak-subjectivity checkpoint because old validator signatures are cheap to recreate after those validators have left. It also says clients have not generally fully validated from genesis for more than five years. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

That makes universal retention a poor proxy for universal verification. Requiring every current node to retain every old body does not make each node execute the whole chain from July 30, 2015. The system already separates a recent trusted starting point from its much larger historical library. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

The benefit has a constitutional flavour. A node that fits on a modest disk is more plausible for a household operator than one that demands an expanding pile of storage. Ethereum.org gives a practical Geth example: about 650 GB after snap sync, growing around 14 GB each week before periodic pruning, alongside a recommendation for a 2 TB drive. [https://ethereum.org/developers/docs/networking-layer/portal-network/]

The cost is a change in default availability. The Foundation says that, before partial expiry, every node stored every block from genesis to the head, giving historical downloads a very high availability guarantee. It now describes a 1-of-N assumption: history can be obtained out of protocol if at least one entity provides the old blocks. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

“At least one” describes integrity and availability differently. A retained header can test whether supplied historical material matches its commitments. It cannot make a missing receipt appear, identify a willing server, pay for its bandwidth, or ensure that a public endpoint has kept its rate limit polite. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://ethereum.org/developers/docs/networking-layer/portal-network/]

That is the argument’s centre: current validation can cost less without making historical retrieval impossible. Calling history public cannot make retrieval costless. The cost moves from every current node to operators who store, index and serve the past. [https://eips.ethereum.org/EIPS/eip-4444] [https://blog.ethereum.org/2025/07/08/partial-history-exp]

WHERE AN OLD RECEIPT GOES WHEN A NODE SAYS NO.

The execution API has already made the absence legible. Its `eth_getTransactionReceipt` documentation reserves error code 4444 for “Pruned history unavailable.” A client can therefore identify a missing retained receipt without treating the transaction as nonexistent. [https://github.com/ethereum/execution-apis/blob/main/docs-api/api/methods/eth_getTransactionReceipt.mdx]

That answer is honest but not sufficient for a relying application. An indexer following a token’s logs, a tool reconstructing an event, or an investigator checking an old transfer still needs another copy. The Foundation identifies institutional providers, torrents and peer-to-peer service by opt-in peers as channels for preserved historical data. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

Each channel solves a different part of the problem. An institutional provider can make a query convenient, but it is a particular service with its own policies. A torrent can distribute a large static archive, but it is not automatically a low-latency query interface. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

The peer-to-peer option is meant to split storage and retrieval across many participants. Ethereum.org describes the Portal Network as a design that shares small pieces of data across a distributed hash table. It aims to avoid a light client relying on one full node or a central RPC provider, and its stated history network covers headers, bodies and receipts. [https://ethereum.org/developers/docs/networking-layer/portal-network/]

That description also marks the uncertainty. Ethereum.org calls Portal a new design and says history expiry, state expiry and statelessness are likely several years from implementation in the context of that page. The protocol’s intended destination should not be reported as a completed, measured guarantee of receipt retrieval. [https://ethereum.org/developers/docs/networking-layer/portal-network/]

The present arrangement is mixed. The Foundation points operators to community-maintained mirrors and torrent files, while Geth allows an operator to keep historical state in archive mode. The record is not confined to a single company, but its convenient retrieval is no longer supplied by every ordinary execution node. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://geth.ethereum.org/docs/fundamentals/archive]

There is a further limit that deserves care. A receipt is not the same thing as every possible historical answer. The Foundation says finding an account’s balance at a past point requires an archive node with specialised indexes, because only current state is maintained by the ordinary node. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

THE KEEPERS OF THE EXPENSIVE COPY.

“Archive node” can sound like one category. Geth documents two materially different forms: a legacy hash-based archive that stores historical state through Merkle Patricia tries, and a path-based archive that stores a full state history through indexed reverse differences. Both address queries about old state, which are a broader task than retaining bodies and receipts. [https://geth.ethereum.org/docs/fundamentals/archive]

The older option carries a price large enough to explain why it is uncommon. Geth says a hash-based mainnet archive can exceed 20 TB and may take months to synchronise from genesis. That figure is client documentation, not a survey of operators, but it describes the burden carried by anyone offering the deepest historical service. [https://geth.ethereum.org/docs/fundamentals/archive]

The newer path-based mode lowers that bill without abolishing it. Geth estimates around 2 TB for complete flat-state history and approximately 6.5 TB when full flat states and historical trie data are both retained; it estimates a path-based sync at around two weeks. Those are implementation estimates from the client team, not a promise about another client or a cloud invoice. [https://geth.ethereum.org/docs/fundamentals/archive]

Receipts alone are cheaper than every past storage slot, but they still need disk, a transaction lookup path and a server prepared to answer queries. Geth’s February 24, 2026 inspection lists 254.76 GiB of ancient receipts and 657.81 GiB of ancient bodies at its quoted height of 22,788,924. The historical service is therefore a real operating function, not a metaphysical property of a hash. [https://geth.ethereum.org/docs/fundamentals/archive]

This gives large providers an obvious role, not an automatic monopoly. An institution, public archive, university, collective of volunteers or commercial RPC service can retain material that a routine node drops. The concern is a keeper set broad enough that one missing account or closed business does not end an enquiry. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://ethereum.org/developers/docs/networking-layer/portal-network/]

That last sentence is an inference from the stated 1-of-N model and Portal’s goal of reducing dependence on central providers. It is not evidence that historical access has already failed or that a particular provider will withdraw it. No open source reviewed here supplies a network-wide measurement of retained receipts, successful retrieval rates, geographic distribution, or the number of independent keepers. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://ethereum.org/developers/docs/networking-layer/portal-network/]

The missing measurements matter more than the slogans. A chain can be cryptographically committed and socially hard to query at the same time. Good history policy should be judged by demonstrated retrieval and verification across independent routes, rather than by storage saved alone. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://eips.ethereum.org/EIPS/eip-4444]

VERIFIABLE DOES NOT MEAN AVAILABLE.

Ethereum has a useful answer to forged history. The Foundation says execution-layer headers remain available from genesis and can cryptographically verify old data; the Portal specifications likewise describe receipt data as checked against the corresponding header fields. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://github.com/ethereum/portal-network-specs]

That is a substantial protection. If a source returns the relevant receipt and the necessary committed data, a client can test it rather than accepting the source’s assertion on faith. The protection applies after retrieval, which is precisely why retrieval remains the policy problem. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://github.com/ethereum/portal-network-specs]

Availability has a more mundane failure mode. A service can be offline, expensive, incomplete, unwilling to serve an old range, or unknown to the person who needs it. None of those outcomes changes a header, and none is refuted by the fact that a correct answer existed on someone else’s disk. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://ethereum.org/developers/docs/networking-layer/portal-network/]

This is not a call to preserve every duplicate forever. The present status quo already depends on specialised infrastructure for some historical state questions, and the Foundation says a current balance or ordinary transaction should not be interrupted by partial history expiry. Making every node pay for rarely used data would be a blunt way to preserve a public good. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

It is a call to name the trade. A light node that requests data from one full node must trust that node, according to Ethereum.org; a Portal-style system aims to reduce that dependency by distributing pieces of the record. The relevant standard is not nostalgia for a heavier disk, but whether the replacement can fetch an old receipt reliably and let the requester verify it. [https://ethereum.org/developers/docs/networking-layer/portal-network/]

Some uses will manage with a transaction hash, a block explorer page, or a provider’s export. Other uses need reproducible access that does not depend on an account at a private API. The protocol documentation establishes the technical routes, but it does not rank these needs or set a universal retention obligation for the people who meet them. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://eips.ethereum.org/EIPS/eip-4444]

The honest uncertainty is simple. Partial expiry exists; full rolling expiry remains work in progress; Portal describes a distribution design rather than a published availability audit. It is too early to declare either that history will become inaccessible or that the replacement has solved access. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://ethereum.org/developers/docs/networking-layer/portal-network/]

THE TEST FOR A PUBLIC RECORD.

The next useful test is practical, not ceremonial. Take a randomly selected old transaction, request its receipt from several ordinary pruned nodes, several independent archives, a public mirror and a peer-to-peer history client. Record whether the answer arrives, whether its proof checks, how much it costs, and what fails. [https://github.com/ethereum/execution-apis/blob/main/docs-api/api/methods/eth_getTransactionReceipt.mdx] [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://ethereum.org/developers/docs/networking-layer/portal-network/]

The test should ask whether a source can retrieve the data. It should ask whether a client can verify the result against Ethereum’s retained commitments. It should ask whether a person without a commercial contract can repeat the process from more than one source. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://github.com/ethereum/portal-network-specs]

The answers will vary by date and by request. A pre-Merge receipt tests the material that partial expiry deliberately targets. A recent receipt tests ordinary service, while a query for a past account balance tests archive-state indexing rather than receipt retention. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://geth.ethereum.org/docs/fundamentals/archive]

Such reporting would also reveal conflicts cleanly. If a provider says it serves full history but returns error 4444 for a known transaction, the claim and the result can be printed together. If a peer-to-peer route returns data that verifies against a retained header, that is evidence of a working alternative, not a promotional adjective. [https://github.com/ethereum/execution-apis/blob/main/docs-api/api/methods/eth_getTransactionReceipt.mdx] [https://blog.ethereum.org/2025/07/08/partial-history-exp]

For now, the record’s custodians are visible but not counted, and Geth offers pruning and archive modes. The Foundation names providers, torrents and peer-to-peer service. Portal proposes a distributed retrieval system, and Eth Docker tells operators that rolling retention can be about five months. [https://geth.ethereum.org/docs/fundamentals/historypruning] [https://geth.ethereum.org/docs/fundamentals/archive] [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://ethereum.org/developers/docs/networking-layer/portal-network/] [https://github.com/ethstaker/eth-docker/releases/tag/v26.10.1]

Those facts support a modest conclusion. Ethereum has not deleted its past in the sense that it has made false history true. It has made preservation a distinct job, and a public chain is only as useful to a late question as the people and systems that still answer it. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://eips.ethereum.org/EIPS/eip-4444]

SOURCES

[https://blog.ethereum.org/2025/07/08/partial-history-exp]
[https://eips.ethereum.org/EIPS/eip-4444]
[https://geth.ethereum.org/docs/fundamentals/historypruning]
[https://geth.ethereum.org/docs/fundamentals/archive]
[https://ethereum.org/developers/docs/networking-layer/portal-network/]
[https://github.com/ethereum/execution-apis/blob/main/docs-api/api/methods/eth_getTransactionReceipt.mdx]
[https://github.com/ethereum/portal-network-specs]
[https://github.com/ethstaker/eth-docker/releases/tag/v26.10.1]

METHOD

This report swept the Ethereum Foundation’s July 8, 2025 announcement, the current EIP-4444 draft, Geth documentation and the execution API specification. It also swept Portal documentation and specifications, and Eth Docker’s October 22, 2026 release; implementation claims rest on documentation by the named client, protocol or operator. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://eips.ethereum.org/EIPS/eip-4444] [https://geth.ethereum.org/docs/fundamentals/historypruning] [https://geth.ethereum.org/docs/fundamentals/archive] [https://ethereum.org/developers/docs/networking-layer/portal-network/] [https://github.com/ethereum/execution-apis/blob/main/docs-api/api/methods/eth_getTransactionReceipt.mdx] [https://github.com/ethereum/portal-network-specs] [https://github.com/ethstaker/eth-docker/releases/tag/v26.10.1] It cuts unverified claims about keeper counts, retrieval success rates, prices and geographic coverage; no secondary reporting is used.

HEADLINE
Ethereum's past needs a maintenance budget.

STANDFIRST
Ethereum can make ordinary nodes cheaper while keeping old transactions open to independent inspection, but those are separate jobs. The case for a maintenance budget follows from that separation: draft EIP-4444 bounds routine history service while leaving preservation incentives and availability checks outside its scope. [https://eips.ethereum.org/EIPS/eip-4444]

The disk comes first.

Matt Garnett's announcement centred on a two-terabyte disk. Writing on the Ethereum Foundation's blog on 8 July 2025, he estimated that discarding pre-Merge block data would save 300–500 gigabytes. That would let an Ethereum node fit comfortably on the disk. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

The announcement offered relief to someone keeping a node running, rather than another promise about transaction throughput. Geth's pruning instructions made the relief concrete: stop the software, remove old block bodies and receipts, then restart. The state database and every header would remain. [https://geth.ethereum.org/docs/fundamentals/historypruning]

A node is a computer running software that checks and exchanges Ethereum data. Its current state contains account balances, contract code and contract storage. Ethereum's archive-node documentation explains that this current state lets clients verify incoming transactions; keeping every earlier state is a separate storage choice. [https://ethereum.org/developers/docs/nodes-and-clients/archive-nodes/]

That distinction matters to the owner of an account that has not moved. Removing a node's old transaction records does not remove the account's current balance or contract data. Geth's pruning guide describes deleting the proof-of-work chain's bodies and receipts while preserving the information needed for continued consensus operation. [https://geth.ethereum.org/docs/fundamentals/historypruning]

Geth's release notes supplied another reason to take storage costs seriously. Version 1.16.0 introduced an experimental archive design whose mainnet state database was estimated at about 1.9 terabytes, excluding transaction and log indexes. The previous design could exceed 20 terabytes and required fast solid-state storage. [https://github.com/ethereum/go-ethereum/releases/tag/v1.16.0]

These figures describe different things: discarded block records and an alternative way to store historical state. They cannot be added into one advertised saving. The comparison shows why the storage argument deserves more respect than a complaint about tidying databases. [https://blog.ethereum.org/2025/07/08/partial-history-exp] [https://github.com/ethereum/go-ethereum/releases/tag/v1.16.0]

The bargain becomes clearer through the archive documentation's account of an old balance query. A full node may need to reconstruct earlier state by executing historical transactions; an archive node keeps earlier states available. Fast answers about the past therefore require additional work even when the underlying transaction records survive. [https://ethereum.org/developers/docs/nodes-and-clients/archive-nodes/]

This gives the storage saving its proper boundary. A machine can hold enough information to check the next transaction without offering convenient access to every earlier account state. The archive documentation describes that trade between storage and reconstruction; public inspection depends on which side of it the requested evidence occupies. [https://ethereum.org/developers/docs/nodes-and-clients/archive-nodes/]

Garnett's disk was a practical benefit, not a distraction from public verification. The mistake would be to treat the saved space as a saving for every participant in every task. Geth's release paired a smaller state archive with new machinery for retrieving expired block history: storage reduction came with replacement work. [https://github.com/ethereum/go-ethereum/releases/tag/v1.16.0]

The window gets smaller.

On 20 August 2026, Eth Docker's version 26.8.1 release changed rolling-expiry settings for Reth, Besu and Erigon. Its notes described retaining 33,024 epochs, approximately five months, instead of a year. This was a change in a package's client configurations, not evidence that every Ethereum node had adopted that window. [https://github.com/ethstaker/eth-docker/releases/tag/v26.8.1]

An epoch is a group of slots in Ethereum's consensus schedule. The consensus specification defines an epoch as 32 slots; the mainnet configuration sets the ordinary slot duration at 12 seconds. These are units of scheduled chain time, not counts of transactions or measurements of archive demand. [https://raw.githubusercontent.com/ethereum/consensus-specs/master/specs/phase0/beacon-chain.md] [https://raw.githubusercontent.com/ethereum/consensus-specs/master/configs/mainnet.yaml]

Then, on 28 September 2026, an amendment to EIP-4444 replaced 33,024 epochs with 14,299. The new proposed window is about 43% of the former window, calculated by dividing the two values in the diff. The amendment changed a draft specification; it did not itself delete anyone's files. [https://github.com/ethereum/EIPs/commit/f951d789d5e2f65ce8ac8994f7e0f4f4affdec43]

The chronology prevents a misleading comparison. Eth Docker's release and the amendment concern different documents, published on different dates, with different authority over running software. A configuration retaining approximately five months and a draft proposing a shorter period are not conflicting measurements that need averaging. [https://github.com/ethstaker/eth-docker/releases/tag/v26.8.1] [https://github.com/ethereum/EIPs/commit/f951d789d5e2f65ce8ac8994f7e0f4f4affdec43]

Read on 31 October 2026, EIP-4444 remained Draft. Its specification says clients should not serve headers, bodies and receipts older than the proposed window through the ordinary peer network; local deletion is permitted. It explains the window by reference to the consensus layer's block-retention requirement. [https://eips.ethereum.org/EIPS/eip-4444]

An associated networking standard shows how partial history can become legible to other computers. EIP-7642, marked Final, adds the earliest and latest available blocks to a peer's status information. A peer can advertise the range it serves instead of making another node discover the boundary through failed requests. [https://eips.ethereum.org/EIPS/eip-7642]

The same standard permits notifications when that range changes. Its authors also describe the information as useful for a crawler counting which nodes retain history. That is a route towards measuring provision, rather than assuming that a connected peer necessarily has the requested past. [https://eips.ethereum.org/EIPS/eip-7642]

This is the news in the smaller number. The September amendment makes the proposed routine window materially shorter than its predecessor, while remaining a proposal. It brings the boundary between ordinary service and separate retrieval closer to the chain's head without establishing how much archival capacity exists beyond it. [https://github.com/ethereum/EIPs/commit/f951d789d5e2f65ce8ac8994f7e0f4f4affdec43]

The old transaction takes another route.

The community history-provider directory gives the past a specific address. For Ethereum's proof-of-work mainnet records, it lists a torrent and mirrors operated under ethPandaOps and Nimbus domains. The listed period runs from genesis on 30 July 2015 to the final pre-Merge block on 15 September 2022. [https://eth-clients.github.io/history-endpoints/]

This is a catalogue, not an uptime certificate. Its publication establishes that retrieval routes are offered; it does not establish their independence, their staffing or their future funding. Those limits matter because a second address is useful only if it can still answer when the first address cannot. [https://eth-clients.github.io/history-endpoints/]

The archive format makes the catalogue more than a collection of screenshots. An Era1 file packages compressed block headers, bodies and receipts, together with difficulty information, an accumulator and an index. The specification caps a batch at 8,192 blocks and records offsets locating entries inside the file. [https://github.com/eth-clients/e2store-format-specs/blob/main/formats/era1.md]

An index is the map from a requested record to its position in storage. That map matters to anyone reconstructing an old transaction: possessing an archive and finding the relevant evidence are different tasks. Era1's explicit block index makes that distinction part of the file format rather than somebody's memory. [https://github.com/eth-clients/e2store-format-specs/blob/main/formats/era1.md]

The format also makes archives portable between implementations that support it. That is an inference from the published layout: a future reader need not guess how a departed operator arranged the records. Preserving the specification alongside the bytes helps distinguish a usable collection from storage whose contents have become somebody else's puzzle. [https://github.com/eth-clients/e2store-format-specs/blob/main/formats/era1.md]

Geth's Download Era guide describes the next part of the route. The operator specifies a server and a block or epoch range; the software obtains the corresponding files and checks them against known checksums. The guide presents selective recovery as an alternative to synchronising the entire chain again. [https://geth.ethereum.org/docs/fundamentals/downloadera]

Consider a researcher seeking a pre-Merge transaction's receipt, the record of its execution result and logs. Ethereum's application interface distinguishes that receipt from the transaction itself and identifies the block containing it. This is an illustrative research task, not a claim that this report recovered a particular transaction. [https://ethereum.org/developers/docs/apis/json-rpc/]

The documented retrieval path is consequently quite ordinary: locate the relevant range, obtain its file, verify it and make the history available locally. Geth's guide requires enough disk space for the downloaded files. The saving for a continuously running node becomes an occasional storage and retrieval requirement for its researcher. [https://geth.ethereum.org/docs/fundamentals/downloadera]

The archive service has also moved beyond the original pre-Merge collection. On the ethPandaOps history page consulted on 31 October 2026, the operator offered an eraE collection covering execution history across the Merge. The page described approximately 1,083 gigabytes across 2,993 files, compared with 427 gigabytes across 1,897 legacy Era1 files. [https://ethpandaops.io/data/history/]

Those are the provider's published collection figures, not measurements of a freshly downloaded archive or proof of coverage through publication. The larger collection is about two and a half times the legacy collection by the page's stated sizes. Its existence is evidence of preservation work already undertaken, not evidence that preservation has no cost. [https://ethpandaops.io/data/history/]

A valid answer still needs a supplier.

The strongest objection to the maintenance argument comes from Garnett's own announcement. He described a “1-of-N trust assumption”: one entity supplying the historical blocks would be enough for nodes to retrieve them outside the usual protocol. He also argued that cryptographic verification protects clients against accepting invalid historical data. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

That defence separates the messenger's identity from a supplied record's truth. But the entity must supply the blocks. Verification describes what can happen after an answer arrives. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

Ethereum's weak-subjectivity documentation explains a related boundary at the start of synchronisation. A new or long-offline proof-of-stake node needs a recent trusted checkpoint to avoid following a misleading alternative history. Weak subjectivity means accepting that initial reference, then checking the chain independently from it. [https://ethereum.org/developers/docs/consensus-mechanisms/pos/weak-subjectivity/]

The documentation suggests cross-checking checkpoints against independent public sources or other nodes. This is not an argument that arbitrary historical files should be accepted because their server seems respectable. It describes how the node identifies the chain against which later checks acquire meaning. [https://ethereum.org/developers/docs/consensus-mechanisms/pos/weak-subjectivity/]

Geth's synchronisation guide makes another useful distinction. Its default snap mode starts from a relatively recent block, while full block-by-block synchronisation executes transactions from genesis. A node that checks new activity successfully therefore has not necessarily repeated every computation that produced Ethereum's entire past. [https://geth.ethereum.org/docs/fundamentals/sync-modes]

These alternatives predate the September amendment. They weaken any account in which shorter history retention suddenly transforms universal replay into trust. The relevant change is narrower: data needed for retrospective work increasingly comes through retrieval arrangements separate from the node's routine job of catching up and checking new blocks. [https://geth.ethereum.org/docs/fundamentals/sync-modes]

A checksum adds another distinction. The provider directory offers SHA-256 hashes for fast file checking and says supporting clients can verify files through import. Matching a published checksum checks agreement with that expected file; the directory does not make a promise that the file will remain downloadable. [https://eth-clients.github.io/history-endpoints/]

The current Portal history specification likewise assumes participants hold historical headers locally to verify supplied bodies and receipts. Other clients need a way to obtain the corresponding header. Its design treats checking content and locating the information needed to check it as related but distinct operations. [https://github.com/ethereum/portal-network-specs/blob/master/history/history-network.md]

The maintenance argument survives the objection in that narrower form. Cryptographic checks can reduce dependence on a supplier's honesty; they do not abolish the task of supplying data. A system designed to reject a false answer still needs someone able to send a true one. [https://github.com/ethereum/portal-network-specs/blob/master/history/history-network.md]

The alternative has a monitor.

Portal offers a serious answer to dependence on a few archive servers. Its repository describes distributing responsibility and letting individual nodes control their resource contribution. The network's purpose is lightweight access to Ethereum data; its specification explicitly describes itself as preliminary rather than a completed service guarantee. [https://github.com/ethereum/portal-network-specs]

The current History Network specification supports retrieval of block bodies and receipts by block number. Nodes track a data radius, which represents the content they are interested in keeping. This is a design for dividing the storage burden rather than requiring every participant to hold the complete archive. [https://github.com/ethereum/portal-network-specs/blob/master/history/history-network.md]

A distributed retrieval network could let a modest machine contribute useful storage without becoming an institutional archive. Portal's repository also describes bridge nodes that inject data, with a planned route from a full node's application interface into Portal. Distribution changes the suppliers' work; it does not eliminate it. [https://github.com/ethereum/portal-network-specs]

Portal's published FAQ gives the reasoning behind its financial design. Its developers say badly designed rewards can encourage participants to extract value instead of improving service. They favour adoption through usefulness and community altruism, citing file-sharing networks as evidence that such participation can work. [https://ethportal.net/resources/faq]

That is an objection to a particular incentive mechanism, not indifference to availability. It deserves an answer stronger than an assumption that unpaid participation always fails. A maintenance budget, in this feature's argument, means sustained provision for storage, bandwidth, software and checking; it need not mean a token or a compulsory fee. [https://ethportal.net/resources/faq]

The FAQ also describes the network as still in development and not fully populated. These are the project's published qualifications, not a live measurement of its completeness on 31 October 2026. They prevent the architecture from serving here as evidence that every requested record already has a dependable alternative route. [https://ethportal.net/resources/faq]

There is a concrete tool for testing the difference. Portal's Glados documentation describes following Ethereum's head, generating content keys and requesting the corresponding records from a Portal client. It records successful and failed requests in a database, making availability something that can be inspected rather than inferred from a diagram. [https://ethportal.net/tooling/glados]

A successful request answers a smaller question than permanent preservation. It shows that a piece of content was retrievable through a particular test; repeated tests could reveal interruptions or missing ranges. This is an inference from Glados's documented method, not a report of results collected by this feature. [https://ethportal.net/tooling/glados]

That instrument changes the argument. The choice is not between trusting a directory and declaring the past lost: the project already describes a way to record whether retrieval works. The maintenance obligation includes keeping such checks running and interpreting their limits alongside the service they observe. [https://ethportal.net/tooling/glados]

The bill is separate from the saving.

The public promise preceded Garnett's disk estimate. In an Ethereum Foundation update published on 29 April 2025, Nixo wrote that long-term history would remain available through archive nodes and Portal. The update also said users could disable pruning, preserving a voluntary route for operators willing to retain the records. [https://blog.ethereum.org/2025/04/29/checkpoint-2]

Read beside the retrieval documentation, that promise identifies a division of labour. Some people operate leaner nodes; others retain, index or distribute what those nodes discard. It does not establish that these are separate people in every case, or that voluntary retention cannot supply enough copies. [https://blog.ethereum.org/2025/04/29/checkpoint-2]

Geth's archive guide shows how much the service definition matters. It distinguishes flat historical state from historical trie data needed for proofs, and makes retention configurable. Its estimates put full flat state history around two terabytes, rising to approximately 6.5 terabytes when historical trie data is included. [https://geth.ethereum.org/docs/fundamentals/archive]

Those estimates cannot price a universal archive service. Answering an old balance query, supplying a proof and distributing raw block files are different deliverables. The guide's distinction implies that counting stored bytes alone would miss whether the retained information can answer the particular question a researcher brings. [https://geth.ethereum.org/docs/fundamentals/archive]

The application interface exposes the difference to its user. A transaction lookup, a receipt lookup, a historical balance request and a log search ask for different information. A public record remains useful for scrutiny only insofar as the relevant evidence can be located and checked, not merely described as retained somewhere. [https://ethereum.org/developers/docs/apis/json-rpc/]

The argument for a maintenance budget is therefore an argument about an identifiable service, not a verified funding shortfall. EIP-4444 explicitly recognises censorship and availability risks and calls for independent preservation and frequent availability checks. It leaves those mechanisms outside its scope. [https://eips.ethereum.org/EIPS/eip-4444]

The documents examined do not establish a durable preservation budget, independent failure domains for every mirror, or retrieval performance across the complete archive. That evidential limit cannot establish that nobody pays, nobody checks, or records have disappeared. EIP-4444 names a responsibility without supplying the mechanism that would settle those questions. [https://eips.ethereum.org/EIPS/eip-4444]

Nor does the existence of cheaper storage settle them automatically. Geth's guide describes historical indexing as necessary before the archive can answer state queries. The relevant uncertainty concerns the continuing delivery of usable evidence, including the software and computation that make stored records answerable. [https://geth.ethereum.org/docs/fundamentals/archive]

No interview with Garnett or an archive operator was conducted for this feature. Their published documents supply the arguments here; operators' accounts and commitments would be needed to establish recurring costs. The documentary record already contains both a storage benefit and a separate preservation obligation, without fixing a price for the latter. [https://blog.ethereum.org/2025/04/29/checkpoint-2]

The node in Garnett's announcement would fit on the disk. Historical retrieval would work if at least one entity provided the blocks. The disk has room; the researcher still needs an answer. [https://blog.ethereum.org/2025/07/08/partial-history-exp]

SOURCES

Ethereum Improvement Proposals, EIP-4444, Draft, consulted on 31 October 2026. [https://eips.ethereum.org/EIPS/eip-4444]
Matt Garnett, Ethereum Foundation, Partial history expiry announcement, 8 July 2025. [https://blog.ethereum.org/2025/07/08/partial-history-exp]
Geth, History Pruning. [https://geth.ethereum.org/docs/fundamentals/historypruning]
Ethereum.org, Ethereum Archive Node. [https://ethereum.org/developers/docs/nodes-and-clients/archive-nodes/]
Go Ethereum, version 1.16.0 release notes. [https://github.com/ethereum/go-ethereum/releases/tag/v1.16.0]
Eth Docker, version 26.8.1 release notes. [https://github.com/ethstaker/eth-docker/releases/tag/v26.8.1]
Ethereum consensus specification, phase-zero beacon chain. [https://raw.githubusercontent.com/ethereum/consensus-specs/master/specs/phase0/beacon-chain.md]
Ethereum consensus mainnet configuration. [https://raw.githubusercontent.com/ethereum/consensus-specs/master/configs/mainnet.yaml]
EIP-4444 amendment, commit f951d789d5e2f65ce8ac8994f7e0f4f4affdec43, 28 September 2026. [https://github.com/ethereum/EIPs/commit/f951d789d5e2f65ce8ac8994f7e0f4f4affdec43]
Ethereum Improvement Proposals, EIP-7642. [https://eips.ethereum.org/EIPS/eip-7642]
Eth-clients, Ethereum history providers. [https://eth-clients.github.io/history-endpoints/]
Eth-clients, Era1 file specification. [https://github.com/eth-clients/e2store-format-specs/blob/main/formats/era1.md]
Geth, Download Era. [https://geth.ethereum.org/docs/fundamentals/downloadera]
Ethereum.org, JSON-RPC API. [https://ethereum.org/developers/docs/apis/json-rpc/]
EthPandaOps, Ethereum History Endpoints. [https://ethpandaops.io/data/history/]
Ethereum.org, Weak subjectivity. [https://ethereum.org/developers/docs/consensus-mechanisms/pos/weak-subjectivity/]
Geth, Sync modes. [https://geth.ethereum.org/docs/fundamentals/sync-modes]
Portal, Execution History Network specification. [https://github.com/ethereum/portal-network-specs/blob/master/history/history-network.md]
Portal, network specification repository and architecture. [https://github.com/ethereum/portal-network-specs]
Portal, FAQ. [https://ethportal.net/resources/faq]
Portal, Glados documentation. [https://ethportal.net/tooling/glados]
Nixo, Ethereum Foundation, Checkpoint update, 29 April 2025. [https://blog.ethereum.org/2025/04/29/checkpoint-2]
Geth, Archive mode. [https://geth.ethereum.org/docs/fundamentals/archive]

METHOD

Reporting on 31 October 2026 swept open specifications, revision records, client documentation, release notes, provider catalogues and principals' announcements; no factual claim rests on secondary reporting. Unverified claims of archive loss, absent funding and universal client adoption were cut; catalogue sizes remain provider figures, and the retrieval example was not executed. The supplied pitches and vote were retained; this draft received an adversarial self-review, but no separate reviewing agent was available.

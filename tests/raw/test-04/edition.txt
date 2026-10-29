LEAD: SEACAST adds tests on larger simulated networks. [https://ethresear.ch/t/26167/2]
TEST EDITION | 29 October 2026

SEACAST author cskiraly published additional broadcast-protocol measurements on 29 October 2026. [https://ethresear.ch/t/26167/2] The update reports tests with more nodes and a second simulator. [https://ethresear.ch/t/26167/2]

cskiraly reports that simulations with 1,000 and 2,000 nodes took about a tenth longer than simulations with 500 nodes. [https://ethresear.ch/t/26167/2] He reports roughly unchanged byte counts across those network sizes. [https://ethresear.ch/t/26167/2] These are simulation results reported by the protocol's author, rather than measurements of Ethereum mainnet deployment. [https://ethresear.ch/t/26167/2]

SEACAST divides objects into coded chunks and forwards each chunk before receiving the complete object. [https://ethresear.ch/t/26167/1] Its design covers both complete-object broadcasts and delivery of samples requested by individual nodes. [https://ethresear.ch/t/26167/1] The original post separates measured implementations, specified rules, formal checks and proposed extensions. [https://ethresear.ch/t/26167/1]

The new update reports that Shadow simulations also put SEACAST ahead of gossipsub on speed and byte consumption across every tested network. [https://ethresear.ch/t/26167/2] cskiraly says corrected code leaves delivery times within the variation between runs. [https://ethresear.ch/t/26167/2] He reports slightly lower byte consumption on thinner links after those fixes. [https://ethresear.ch/t/26167/2]

The added comparison includes FullDAS with every node sampling every cell, a specific configuration rather than all possible sampling workloads. [https://ethresear.ch/t/26167/2] cskiraly reports SEACAST was faster and lighter across ten simulated networks of each tested kind. [https://ethresear.ch/t/26167/2] The original timing definition excludes proof checking, block waiting and decoding, limiting what these delivery figures establish. [https://ethresear.ch/t/26167/1]

ALSO TODAY:
[WALLETS] An ERC draft proposes independent signing checks. [https://ethresear.ch/t/26192]
The 28 October 2026 post proposes structured transaction intent, independent simulation and revocable permissions for privileged operations. [https://ethresear.ch/t/26192] Its stated status is Draft; its verification requirements describe a proposed interface. [https://ethresear.ch/t/26192]

[MEASUREMENT] TEMBRI adds contract-update and trade pairing. [https://ethresear.ch/t/26156/14]
Dan Guo's 28 October 2026 update describes pairing updates and fills within the same block and pool. [https://ethresear.ch/t/26156/14] Guo explicitly limits the result to on-chain receipt order, excluding proof of off-chain quote freshness or builder receipt time. [https://ethresear.ch/t/26156/14]

[ENCRYPTION] A mempool proposal narrows its release window. [https://ethresear.ch/t/26169/2]
Arian Araghi's 28 October 2026 correction gives roughly eight to nine seconds before the next builder's payload commitment. [https://ethresear.ch/t/26169/2] The proposed release mechanism puts time-locks on committee key shares; its hardware-speed assumption remains unmeasured, according to the author. [https://ethresear.ch/t/26169/1]

READING LIST:
[https://ethresear.ch/t/26167/2] Read the new simulation comparisons and their configurations.
[https://ethresear.ch/t/26192] Examine the draft's proposed signing workflow.
[https://ethresear.ch/t/26156/14] Read the boundary between observed ordering and quote freshness.
[https://ethresear.ch/t/26169/1] Check the release mechanism's hardware and cryptographic assumptions.

METHOD:
Swept Ethereum Research, the Ethereum Foundation blog and all three linked prior editions; the target window covered 48 hours, 27 October 2026 10:00 UTC to 29 October 2026 10:00 UTC. [https://ethresear.ch/latest] [https://blog.ethereum.org/archive] [https://openinterest-ai.github.io/paper/rehearsal.html] Prior leads covered Hoodi and stateless workers; this lead uses the distinct 29 October 2026 SEACAST update, with older technical context explicitly sourced. [https://openinterest-ai.github.io/paper/tests/test-03.html] [https://ethresear.ch/t/26167/2] Cut the STVA author's theft-prevalence claim for failed independent verification; all included technical claims rest on primary authors, with no secondary-source dependencies or independently rerun experiments. [https://ethresear.ch/t/26192]

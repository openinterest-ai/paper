LEAD: A researcher proposes authorization without signatures. [https://ethresear.ch/t/26196/1]
TEST EDITION | 31 October 2026

A 30 October 2026 research post proposes authorizing actions through fresh proofs of knowledge of a reusable secret. [https://ethresear.ch/t/26196/1] Its author presents a conditional quantum-security argument and implementation measurements, while inviting scrutiny of the assumptions. [https://ethresear.ch/t/26196/1]

The author, ignotusnemo, describes a public commitment to a secret, with each proof bound to the requested action. [https://ethresear.ch/t/26196/1] Applications specify the operation, context and execution constraints, then enforce freshness through a nonce, counter or resource reference. [https://ethresear.ch/t/26196/1] The construction requires independent fresh randomness for every authorization attempt, including abandoned attempts. [https://ethresear.ch/t/26196/1]

The reported quantum-security reduction assumes a particular idealized permutation model and additional conditions on the authority circuit. [https://ethresear.ch/t/26196/1] The author explicitly seeks cryptanalysis of those conditions and the difficulty of recovering the authority secret. [https://ethresear.ch/t/26196/1]

For a payment fixture with one input and one output, the author reports median proving of 893.8 milliseconds. [https://ethresear.ch/t/26196/1] Median verification was 25.59 milliseconds, excluding serialization and decoding; measurements used four CPU threads on an Intel Core i7-1365U. [https://ethresear.ch/t/26196/1] Those timings describe the reported implementation and hardware, rather than a matched comparison against post-quantum signatures. [https://ethresear.ch/t/26196/1]

The author proposes combining authorization proofs with execution proofs and identifies Ethereum integration as an open question. [https://ethresear.ch/t/26196/1] The post requests comparisons under matched hardware and security assumptions, leaving the relative cost unresolved. [https://ethresear.ch/t/26196/1]

ALSO TODAY:

[WALLETS] A draft makes transaction simulations reproducible. [https://ethresear.ch/t/26198/1]
The 30 October 2026 STVA draft proposes canonical results bound to transaction inputs and a state snapshot. [https://ethresear.ch/t/26198/1] On 31 October 2026, Micah Zoltu asked how a signing device would anchor its trust in the supplied state witness. [https://ethresear.ch/t/26198/2] The question identifies a trust requirement that the opening proposal leaves for discussion. [https://ethresear.ch/t/26198/1] [https://ethresear.ch/t/26198/2]

[PERMISSIONS] A draft scopes authority to specific actions. [https://ethresear.ch/t/26195/1]
The STVA capability-token post, published on 30 October 2026, proposes permissions with expiry, scope checks and revocation. [https://ethresear.ch/t/26195/1] Simulation-result binding is optional in its core fields, while its strict compliance level requires that binding. [https://ethresear.ch/t/26195/1]

[ACCOUNTS] A proposal permanently disables account delegation. [https://ethereum-magicians.org/t/30134/1]
The 30 October 2026 draft proposes an account-code marker that prevents subsequent EIP-7702 delegation while retaining ordinary transactions. [https://ethereum-magicians.org/t/30134/1] Its author says the mechanism would not prevent a compromised key from transferring funds. [https://ethereum-magicians.org/t/30134/1] A commenter warns that the protection would apply separately on each chain and could disrupt safe NFT transfers. [https://ethereum-magicians.org/t/30134/2]

READING LIST:

[https://ethresear.ch/t/26196/1] Read the model assumptions and benchmark boundaries behind the authorization proposal.
[https://ethresear.ch/t/26198/2] Read the signing-device trust question before treating reproducibility as settled.
[https://ethresear.ch/t/26195/1] Compare optional simulation binding with the strict compliance requirements.
[https://ethereum-magicians.org/t/30134/2] Examine the commenter's objections to an irreversible account setting.

METHOD:
Swept Ethereum Research, Ethereum Magicians and the rehearsal archive; the target window covered 48 hours, 29 October 2026 06:40 UTC to 31 October 2026 06:40 UTC. [https://ethresear.ch/latest] [https://ethereum-magicians.org/latest] [https://openinterest-ai.github.io/paper/rehearsal.html] Read all four linked prior editions before drafting; none led with signatureless authorization. [https://openinterest-ai.github.io/paper/tests/test-01.html] [https://openinterest-ai.github.io/paper/tests/test-02.html] [https://openinterest-ai.github.io/paper/tests/test-03.html] [https://openinterest-ai.github.io/paper/tests/test-04.html] Cut the capability author's claim about approvals' prevalence in high-value losses for lack of independent verification. [https://ethresear.ch/t/26195/1] Technical claims remain attributed to proposal authors; the delegation cautions rest on a discussion reply, without independent reproduction. [https://ethereum-magicians.org/t/30134/2] No included claim relies on secondary news reporting; benchmarks and proofs were not independently rerun.

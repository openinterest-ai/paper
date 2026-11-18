OPEN INTEREST | 18 November 2026 | v2

LEAD
A judge acquits the brothers in Ethereum's $25 million trading case. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=1]

Judge Jessica Clarke entered judgments of acquittal for Anton and James Peraire-Bueno on November 16, 2026. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=46] She found that prosecutors failed to prove a material misrepresentation, an essential element of their wire-fraud case. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=1]

The ruling clears both defendants of wire fraud, conspiracy to commit wire fraud and conspiracy to commit money laundering. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=46] Their trial had ended with a deadlocked jury; Clarke then considered whether the government's evidence could legally sustain convictions. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=1]

The case concerned an April 23, 2023 operation called Omakase, which targeted automated traders on Ethereum. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=2] The court describes bait transactions that attracted bots seeking profits by placing trades around other users' transactions. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=2] The brothers exploited a software vulnerability to inspect private transactions, then substituted trades that defeated the bots' strategy. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=3]

The opinion puts the resulting gain at $25 million in twelve seconds, the operation's execution time. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=1] But Clarke rejected the government's proposed falsehoods, including theories about validator registration, block queries and the submission of a modified block. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=41] Frustrating MEV-Boost's intended design did not itself establish the misrepresentation required for fraud, she wrote. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=41]

Prosecutors also pointed to concealment and evidence that the brothers knew their conduct was wrong. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=45] Clarke held that fraudulent intent could not replace proof of a material falsehood. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=45] The laundering conspiracy failed because its alleged criminal proceeds depended on the wire-fraud charge. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=46]

Clarke expressly separated this decision from whether the conduct was moral or violated crimes prosecutors had not charged. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=1] She noted serious due-process concerns but did not decide that constitutional question. [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf#page=22]

NEWS

[NEWS] Optimizely removes malicious code from customer projects. [https://status.optimizely.com/incidents/ftw0fh9wx43z]
Optimizely says it fixed a vulnerability that let an unauthorized party insert JavaScript into customer projects. [https://status.optimizely.com/incidents/ftw0fh9wx43z] Report URI's Scott Helme found infected code in 188 of 1,611 examined scripts, covering 178 organizations, including Ledger. [https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/] He reports that the code replaced cryptocurrency addresses on pages and clipboards with attacker-controlled destinations. [https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/]

His November 17, 2026 update says all infected files his team found were clean by November 16, 2026, 23:11 UTC. [https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/]

[NEWS] The CFTC suspends Kalshi's Trump speech contracts. [https://www.cftc.gov/filings/documents/2026/orgdcmkexorderinstproce261116.pdf]
The CFTC stayed the listing of Kalshi's Trump nickname market and TRUMPSAY series while examining their compliance certification. [https://www.cftc.gov/filings/documents/2026/orgdcmkexorderinstproce261116.pdf] Its order says Kalshi has not adequately demonstrated that these contracts resist manipulation. [https://www.cftc.gov/filings/documents/2026/orgdcmkexorderinstproce261116.pdf] Kalshi must answer by December 11, 2026; the order makes no final finding that the contracts violate federal law. [https://www.cftc.gov/filings/documents/2026/orgdcmkexorderinstproce261116.pdf]

CEO Tarek Mansour disputes the decision, arguing that presidential remarks have economic significance, according to Cointelegraph's November 17, 2026 report. [https://cointelegraph.com/news/cftc-kalshi-trump-mention-markets-review]

[NEWS] The World Bank brings Circle and Citi into its payments exploration. [https://www.worldbank.org/en/news/press-release/2026/11/17/world-bank-group-explores-regulated-stablecoins-to-modernize-payments-redirect-res]
The World Bank Group announced the collaboration on November 17, 2026, to examine stablecoins alongside its existing cross-border disbursement arrangements. [https://www.worldbank.org/en/news/press-release/2026/11/17/world-bank-group-explores-regulated-stablecoins-to-modernize-payments-redirect-res] Citi would connect banking infrastructure, while Circle would supply infrastructure for issuing and settling USDC. [https://www.worldbank.org/en/news/press-release/2026/11/17/world-bank-group-explores-regulated-stablecoins-to-modernize-payments-redirect-res] The initial exploration concerns an intermediated model in borrower countries that permit digital assets; the announcement supplies no measured savings. [https://www.worldbank.org/en/news/press-release/2026/11/17/world-bank-group-explores-regulated-stablecoins-to-modernize-payments-redirect-res]

TECH

[TECH] Kiraly's simulations expose the bandwidth cost of proof aggregation. [https://ethresear.ch/t/eip-8288-the-networking-side-of-recursive-aggregation/26263]
Csaba Kiraly's November 18, 2026 study models EIP-8288, which would combine transaction-verification work into shared cryptographic proofs. [https://ethresear.ch/t/eip-8288-the-networking-side-of-recursive-aggregation/26263] At fifteen signature transactions per second, pushing proofs to six peers consumed 11.9–13.3 megabits per second per node in the tested networks. [https://ethresear.ch/t/eip-8288-the-networking-side-of-recursive-aggregation/26263] Kiraly argues that specifications must define who aggregates, when peers fetch proofs and which prover hardware sets the interval. [https://ethresear.ch/t/eip-8288-the-networking-side-of-recursive-aggregation/26263]

These are simulator results across proposed designs, not measurements of a deployed Ethereum upgrade. [https://ethresear.ch/t/eip-8288-the-networking-side-of-recursive-aggregation/26263]

[TECH] Santos tests alternative quantum-resistant signatures inside Ethereum proofs. [https://ethresear.ch/t/exploring-post-quantum-signature-aggregation-for-eip-8288/26261]
Manuel B. Santos published experimental leanVM measurements for five signature schemes on November 16, 2026. [https://ethresear.ch/t/exploring-post-quantum-signature-aggregation-for-eip-8288/26261] Raccoon-G verification exceeded the implementation's witness limit, requiring separate proofs that the experiment then combined. [https://ethresear.ch/t/exploring-post-quantum-signature-aggregation-for-eip-8288/26261] Santos sketches wallets retaining signing keys while external aggregators perform proving, but notes that EIP-8288's generic proof path remains incomplete. [https://ethresear.ch/t/exploring-post-quantum-signature-aggregation-for-eip-8288/26261]

CULTURE

[CULTURE] Neuder challenges Ethereum's proposed quantum deadline. [https://hackmd.io/@mikeneuder/thoughts-on-pqai27]
Mike Neuder's November 15, 2026 essay argues that rushing quantum resistance could undermine promises already made through Ethereum's upgrade process. [https://hackmd.io/@mikeneuder/thoughts-on-pqai27] Ethlabs proposes readiness in 2027 and says other features must be reconsidered, including FOCIL, a proposed censorship-resistance mechanism. [https://ethereum-magicians.org/t/an-ethlabs-view-on-post-quantum-and-post-ai-timelines-pqai27/30351] Neuder favors hardening existing software immediately and targeting quantum resistance in 2028; he says dropping FOCIL would damage governance credibility. [https://hackmd.io/@mikeneuder/thoughts-on-pqai27]

[CULTURE] White disputes the crypto lobby's election victory narrative. [https://www.citationneeded.news/crypto-ai-lost-the-midterms/]
Molly White's November 13, 2026 analysis challenges Fairshake's advertised success by separating competitive races from safer bets. [https://www.citationneeded.news/crypto-ai-lost-the-midterms/] Her tally gives Fairshake victories in all 74 races with clear or likely favorites, against ten of eighteen competitive races across election rounds. [https://www.citationneeded.news/crypto-ai-lost-the-midterms/] White reports that Fairshake nevertheless claimed a meaningful role in competitive victories; her methodology uses reported spending and race ratings, rather than proving electoral causation. [https://www.citationneeded.news/crypto-ai-lost-the-midterms/]

READING LIST

[https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf] Clarke's opinion distinguishes an exploit from the specific falsehood required for wire fraud.
[https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/] Helme supplies the attack timeline, recipient addresses and limits of the loss evidence.
[https://ethresear.ch/t/eip-8288-the-networking-side-of-recursive-aggregation/26263] Kiraly documents the networking assumptions behind the proof-aggregation simulations.
[https://hackmd.io/@mikeneuder/thoughts-on-pqai27] Neuder sets out the governance objection and an alternative timetable.

METHOD

We swept news feeds, official records and research forums for November 16, 2026, 00:00 UTC through November 18, 2026, 10:30 UTC, covering 58.5 hours. [https://www.coindesk.com/arc/outboundfeeds/rss/] [https://cointelegraph.com/rss] [https://ethresear.ch/latest.json] We checked the rehearsal's linked editions and masthead; older essays supply context, and the lead uses the court opinion reproduced by Decrypt. [https://openinterest-ai.github.io/paper/rehearsal.html] [https://raw.githubusercontent.com/openinterest-ai/paper/main/masthead/voices.csv] [https://wp.decrypt.co/wp-content/uploads/2026/11/11162026peraire.pdf] We cut unverified total-loss and AI-attribution claims for Optimizely; Mansour's response rests on Cointelegraph, and White's attributed Fairshake response is secondhand. [https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/] [https://cointelegraph.com/news/cftc-kalshi-trump-mention-markets-review] [https://www.citationneeded.news/crypto-ai-lost-the-midterms/]

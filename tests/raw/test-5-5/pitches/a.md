Who keeps Ethereum’s receipts?

The argument: Ethereum can make verification cheaper while making its past harder to retrieve independently. History expiry shifts the preservation bill to whoever still needs old evidence. That is an inference to test, grounded in ethereum.org’s distinction between data availability and permanent retrievability [https://ethereum.org/developers/docs/data-availability/].

Why now: Eth Docker’s 22 October 2026 release makes its rolling-expiry warning more explicit: roughly five months of retained execution history [https://github.com/ethstaker/eth-docker/releases/tag/v26.10.1]. This is an operator-facing change, not a claim that Ethereum erased its past. EIP-7642 specifies how peers announce the historical block range they serve [https://eips.ethereum.org/EIPS/eip-7642].

The consequence is practical: someone investigating an old transaction needs its evidence, even when validators no longer need it. Geth’s History Pruning documentation says pre-Merge bodies and receipts can be removed while headers and state remain [https://geth.ethereum.org/docs/fundamentals/historypruning]. Its Download Era documentation describes retrieving expired history from servers [https://geth.ethereum.org/docs/fundamentals/downloadera].

Readers learn where verification ends and retrieval begins. The feature will follow an old receipt through preservation, retrieval, and authentication, then identify who pays. Whether independent copies provide dependable access remains unanswered; documentation establishes mechanisms, not service reliability.

The fresh angle is custody of evidence, rather than another upgrade preview. It avoids every prior rehearsal lead [https://openinterest-ai.github.io/paper/rehearsal.html]. All five technical sources above are checked, open, primary documents; no secondary reporting supports this pitch.

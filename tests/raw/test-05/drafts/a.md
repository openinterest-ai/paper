TEST EDITION | 31 October 2026

LEAD: Aave froze its markets after a Binance hot-wallet drain.

LlamaRisk says an address that drained Binance hot wallets on 29 October 2026 borrowed 19,762 WETH on Aave before guardians froze 292 reserves [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. A four-wave unfreeze is under way, with the exploiter's assets barred from backing new borrows [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18].

At 20:24 UTC on 29 October 2026, a Binance hot wallet sent 167,464 ETH to a single address in one transaction, according to Aave risk provider LlamaRisk [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. The same address received 28,006 ETH from a second Binance hot wallet, plus funds on Arbitrum, Optimism and Avalanche [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. LlamaRisk calls that address the exploiter; Binance's own account was not verified for this edition.

Between 20:58 and 21:01 UTC, one wallet in that cluster supplied 60M USDT and borrowed 19,762 WETH, about $44.6M at the time [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. LlamaRisk reports $59.9M of collateral against $43.8M of debt, so the position stays subject to normal liquidation [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954].

Guardian multisigs froze 175 reserves on Aave V3 across 16 networks and 117 on Aave V4 between 21:42 and 23:04 UTC [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. LlamaRisk chose a freeze because guardians can reverse it, while cap cuts would need about five days of governance to restore [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954].

Withdrawals during the freeze pushed the largest reserves to 92% to 100% utilization, so stewards capped borrow rates at 10.00% APR [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18] [https://governance.aave.com/t/risk-stewards-temporary-slope2-reductions-on-aave-v3-and-aave-v4-2026-10-30/25955]. A second batch removed about $3.7B of unused V3 borrow capacity [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18] [https://governance.aave.com/t/risk-stewards-borrow-and-draw-cap-reductions-on-aave-v3-and-aave-v4-2026-10-30/25960]. USDT, USDC and seven other assets held by the exploiter's cluster stay at zero borrowing power [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18].

Forum respondents propose borrow velocity limits; those remain individual suggestions, not governance proposals [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/11].

ALSO TODAY:

[CRYPTOGRAPHY] A researcher proposes post-quantum authorization without signatures.
ignotusnemo's 30 October 2026 post replaces signatures with fresh zero-knowledge proofs of knowledge of a committed secret, bound to each action [https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196]. The author reports median proving near 0.9 seconds and verification near 25.6 ms on a laptop CPU, with capsules up to 92,696 bytes [https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196]. A respondent cites earlier work on the idea; the author says the new contribution is a concrete protocol, implementation and security reduction [https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196/3].

[WALLETS] The STVA signing-check draft gains two companion standards.
Test 04 covered the base draft [https://openinterest-ai.github.io/paper/tests/test-04.html]; the new angle is that its author added scoped capability tokens on 30 October 2026 and a canonical simulation-result format the same day [https://ethresear.ch/t/scoped-capability-tokens-for-stva/26195] [https://ethresear.ch/t/erc-draft-independent-simulation-result-for-stva/26198]. On 31 October 2026, MicahZoltu asked how a signing device would anchor trust in the supplied state witness [https://ethresear.ch/t/erc-draft-independent-simulation-result-for-stva/26198/2]. That question has no published answer yet.

[ACCOUNTS] A draft EIP lets accounts permanently refuse EIP-7702 delegation.
EIP-8476, posted on 30 October 2026, installs a fixed 3-byte marker through a set-code transaction costing 33,500 gas [https://ethereum-magicians.org/t/eip-8476-permanent-eoa-delegation-opt-out/30134]. A reviewer notes the marker binds only one chain, and that marked accounts could no longer receive some ERC-1155 and ERC-721 transfers [https://ethereum-magicians.org/t/eip-8476-permanent-eoa-delegation-opt-out/30134/2].

READING LIST:
[https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954] The primary incident log, with transaction links and freeze timings.
[https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18] The four-wave unfreeze plan and the list of restricted assets.
[https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196] The security model and measured costs behind signatureless authorization.
[https://ethereum-magicians.org/t/eip-8476-permanent-eoa-delegation-opt-out/30134] The review exposes per-chain and token-receipt limits of an irreversible opt-out.

METHOD: The sweep covered Ethereum Research, Ethereum Magicians, the Aave and Lido governance forums, the Ethereum Foundation blog and the rehearsal archive, targeting 29 October 2026 to 31 October 2026, a 48-hour window [https://openinterest-ai.github.io/paper/rehearsal.html]. Prior tests led with Hoodi's postponement, the L1.5 proposal and SEACAST, so none was re-led. The Foundation blog and Lido forum showed no new posts in the window. All exploit figures rest on LlamaRisk, a service provider to the frozen protocol; this edition did not replay transactions. Claims of Binance's confirmed loss total and recovery status were cut for failed verification on open platforms. Price moves from social posts were cut as unverified. Post-quantum performance figures are the author's own measurements. The fetched house guide governed drafting [https://raw.githubusercontent.com/openinterest-ai/paper/main/style-guide.html].

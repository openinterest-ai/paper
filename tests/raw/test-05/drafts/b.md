TEST EDITION | 31 October 2026

LEAD: Aave froze its markets after a Binance hot wallet drain.

An exploiter who drained Binance hot wallets on 29 October 2026 borrowed 19,762 WETH on Aave before the freeze, according to Aave risk provider LlamaRisk. Guardians froze 292 reserves across Aave V3 and V4, and a staged reopening began on 30 October 2026.

At 20:24 UTC on 29 October 2026, a Binance hot wallet on Ethereum sent 167,464 ETH to a single address, LlamaRisk reports [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. It traces a further 28,006 ETH from a second Binance wallet and 444,537 AVAX on Avalanche at 23:04 UTC [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. These Binance-side figures are LlamaRisk's tracing; this edition found no Binance statement on an open platform.

Between 20:58 and 21:01 UTC, one exploiter wallet supplied 60M USDT and borrowed WETH worth about $44.6M [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. LlamaRisk says the position holds $59.9M of collateral against $43.8M of debt, so it remains over-collateralised and liquidatable [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954].

Guardian multisigs froze 175 reserves on 16 V3 networks and 117 on four V4 networks between 21:42 and 23:04 UTC [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954]. LlamaRisk chose a freeze because the guardian can reverse one, while cap cuts would need about five days of governance to restore [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954].

Frozen markets drew withdrawals that pushed big reserves to 92% to 100% utilisation, LlamaRisk reports [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18]. Stewards temporarily held full-utilisation borrow rates to 10.00% APR [https://governance.aave.com/t/risk-stewards-temporary-slope2-reductions-on-aave-v3-and-aave-v4-2026-10-30/25955]. They cut the largest borrow caps to about 2% above pre-exploit borrowing, removing about $3.7B of unused V3 capacity [https://governance.aave.com/t/risk-stewards-borrow-and-draw-cap-reductions-on-aave-v3-and-aave-v4-2026-10-30/25960] [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18].

The reopening keeps USDT, USDC and seven other assets held by the exploiter's cluster at zero borrowing power as collateral [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/18]. Forum members split over borrowing velocity limits [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/11] against treating the freeze as an overreaction [https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954/5]. No date for restoring those assets' collateral value has been published.

ALSO TODAY:

[CRYPTOGRAPHY] A researcher proposes post-quantum authorization without signatures.
ignotusnemo's 30 October 2026 post replaces signatures with fresh zero-knowledge proofs of a reusable secret, each bound to one requested action [https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196]. The author reports median proving of 893.8 ms and verification of 25.59 ms on an Intel Core i7-1365U, with capsules up to 92,696 bytes [https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196]. A commenter cited earlier signature-free work; the author replied that this construction differs and adds a quantum security reduction [https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196/2] [https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196/3].

[WALLETS] The STVA wallet-security drafts now include simulation results that anyone can recompute.
Test 04 covered the original STVA draft; the new angle is a 30 October 2026 companion ERC defining a canonical, hashable simulation result that an offline device must re-verify [https://ethresear.ch/t/erc-draft-independent-simulation-result-for-stva/26198]. A separate draft binds that hash into short-lived capability tokens [https://ethresear.ch/t/scoped-capability-tokens-for-stva/26195]. On 31 October 2026, Micah Zoltu asked how a signing device would anchor its trust in the state witness to a recent block hash [https://ethresear.ch/t/erc-draft-independent-simulation-result-for-stva/26198/2].

[LISTINGS] Aave Labs rates tokenized Tesla shares technically eligible on Base.
Its assessment, dated 23 October 2026 and posted 29 October 2026, finds TSLAc eligible for listing on Base [https://governance.aave.com/t/tokenized-tesla-inc-shares-tslac-on-aave-base-assessments/25942/2]. It flags a price feed available 24 hours a day, five days a week, issuer controls without an onchain timelock, and permissioned redemption [https://governance.aave.com/t/tokenized-tesla-inc-shares-tslac-on-aave-base-assessments/25942/2]. Eligibility is a technical finding, not a listing decision.

READING LIST:
[https://governance.aave.com/t/binance-hot-wallet-exploit-aaves-response/25954] The primary incident log, with timestamps and reserve counts.
[https://governance.aave.com/t/risk-stewards-borrow-and-draw-cap-reductions-on-aave-v3-and-aave-v4-2026-10-30/25960] Every cap cut, listed reserve by reserve.
[https://ethresear.ch/t/post-quantum-signatureless-authorization-with-recursive-verification/26196] The security model and the cryptanalysis the author requests.
[https://ethresear.ch/t/erc-draft-independent-simulation-result-for-stva/26198] The draft's three compliance levels and its open questions.

METHOD: The sweep covered Ethereum Research, the Ethereum Foundation blog, the Aave governance forum, the Lido research forum and the rehearsal archive, for 29 October 2026 00:00 UTC to 31 October 2026 07:00 UTC [https://openinterest-ai.github.io/paper/rehearsal.html]. Prior editions led with Hoodi's postponement, stateless computation workers and SEACAST; none led with this incident. STVA appears only with its new companion drafts. Every Binance-side figure rests on LlamaRisk's tracing, which is secondary for Binance; no Binance statement was found on an open platform. Aave's freeze, caps and rate changes come from the stewards' own posts. Cut for failed verification: a forum claim about the size of Binance's holdings, and a claim about a risk provider's departure that rested on one news site. The Lido Lend thread was not read in full and was excluded. Exploiter identity and recovery prospects remain unanswered.

OPEN INTEREST
Daily brief, format v2. Monday, 16 November 2026.

LEAD

Attackers turned Luxor's fleet software against its own miners.

Hijacked bitcoin machines mined for an attacker's address on the OCEAN pool for hours on 15 November 2026. The machines found no block, yet the address has collected about 0.32 BTC from OCEAN's payout rules.

Luxor says its internal monitoring caught "an unauthorized redirect of hashrate through Commander," its software for managing mining fleets [https://news.bitcoin.com/security/luxor-confirms-bitcoin-mining-hack-and-reveals-ai-enabled-attack/]. The company puts the impact at "just over a dozen client accounts" and says no data left its systems [https://news.bitcoin.com/security/luxor-confirms-bitcoin-mining-hack-and-reveals-ai-enabled-attack/]. It says engineers patched Commander within two hours and that affected clients will be compensated for lost revenue [https://news.bitcoin.com/security/luxor-confirms-bitcoin-mining-hack-and-reveals-ai-enabled-attack/].

The outside estimate is far larger. CoreX Hosting, which raised the first alarm, put the damage at about 64,000 machines and roughly 13 EH/s of hashrate, BeInCrypto reported [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/]. Luxor has not confirmed those figures, so the scope stands as a range between a dozen accounts and CoreX's count [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/].

Luxor chief executive Nick Hansen says the compromise began around 18:00 PDT on 14 November 2026 and came "through a sophisticated AI-enabled vector" [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/]. Luxor has published no technical account of that vector, and this paper could not test the claim [https://news.bitcoin.com/security/luxor-confirms-bitcoin-mining-hack-and-reveals-ai-enabled-attack/].

The chain shows the money. The attacker's address, bc1qphukp9rjfc4rcej7erpm9ae20xmtspw8pcddrr, has received four payments totalling 0.32445584 BTC [https://mempool.space/address/bc1qphukp9rjfc4rcej7erpm9ae20xmtspw8pcddrr]. They landed in blocks 975,995 through 976,097, the first at 17:22 UTC on 15 November 2026 and the last at 08:17 UTC on 16 November 2026 [https://mempool.space/tx/663bdc6bebc3e88eb38f1c7460018c150ba01bfedb0ccd73195d25753875475f]. OCEAN pays recent contributors whenever the pool finds a block, which is why work that found nothing still pays [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/].

The sum is small. The exposure is not: one management console sat between thousands of machines and a stranger's payout address, and OCEAN had not publicly addressed the payouts when BeInCrypto published [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/].

NEWS

[NEWS] Coinone discloses a customer data leak through its support contractor.
South Korean exchange Coinone said on 15 November 2026 that an outside attacker entered the servers of the contractor handling its customer support [https://coinone.co.kr/info/notice/5950]. The intrusion occurred around 04:00 KST on 12 November 2026, and the exposed categories include passwords, bank account numbers, resident registration numbers and wallet addresses, Bitcoin.com News reported from the notice [https://news.bitcoin.com/security/coinone-data-breach-exposes-passwords-and-sensitive-customer-records/]. Coinone says its trading systems and wallets run separately from the contractor's servers [https://news.bitcoin.com/security/coinone-data-breach-exposes-passwords-and-sensitive-customer-records/]. It has not said how many customers are affected [https://news.bitcoin.com/security/coinone-data-breach-exposes-passwords-and-sensitive-customer-records/].

[NEWS] BitGo says Unocoin's disputed transfers were signed with Unocoin's own keys.
In a statement on 13 November 2026, BitGo said the outgoing transactions were "signed using the user and backup keys held by Unocoin" and broadcast without BitGo's participation, crypto.news reported [https://crypto.news/bitgo-unocoin-transfers-client-held-keys/]. The Indian exchange's wallets use a two-of-three arrangement, so its two keys could move funds while the account freeze BitGo applied on 6 November 2026 still held [https://crypto.news/bitgo-unocoin-transfers-client-held-keys/]. BitGo's own recovery documentation describes signing without BitGo using the user and backup keys [https://github.com/BitGo/wallet-recovery-wizard/blob/master/NON_BITGO_RECOVERY.md]. Unocoin has given no loss figure, and neither party names who used the keys [https://thecryptodesk.substack.com/p/the-crypto-desk-saturday-14-november].

[NEWS] SEC enforcement fell to 348 actions in fiscal 2026.
The SEC reported 348 enforcement actions for fiscal 2026, down 23.7% from 456 in fiscal 2025, according to Lowenstein Sandler's summary of the agency's annual results [https://www.lowenstein.com/news-insights/newsletters/crypto-brief-november-12-2026]. The crypto cases it highlighted are fraud cases, including three purported trading platforms and four investment clubs accused of taking at least $14 million from retail investors [https://www.sec.gov/newsroom/press-releases/2026-113-sec-announces-enforcement-annual-results-fiscal-year-2026]. It also cited a bitcoin mining founder accused of misappropriating $48.5 million of the more than $95.6 million raised from about 6,400 investors [https://www.lowenstein.com/news-insights/newsletters/crypto-brief-november-12-2026]. Registration disputes, the core of the agency's crypto docket in earlier years, are absent from that list [https://www.lowenstein.com/news-insights/newsletters/crypto-brief-november-12-2026].

TECH

[TECH] Csaba Kiraly argues Ethereum should size its capacity to measured network load.
In an opinion post on 11 November 2026, Kiraly writes that Ethereum fixes its capacity in advance and has no protocol-wide rule that adapts limits to measured resource pressure [https://ethresear.ch/t/elastic-ethereum/26236]. He cites mainnet data showing the median block reaching 95% of reporting nodes 0.38 seconds after first sighting, against a 4-second attestation deadline [https://ethresear.ch/t/elastic-ethereum/26236]. His model is TCP congestion control, which backs off under load and so can run close to what the network carries [https://ethresear.ch/t/elastic-ethereum/26236]. He labels it a design direction, not a specification [https://ethresear.ch/t/elastic-ethereum/26236].

[TECH] An EF-mentored paper tests whether Ethereum needs more fee meters or better prices.
Fei Wu's paper, posted on 12 November 2026 with mentoring from EF researcher Maria Silva, compares tuned one-dimensional fee markets against EIP-7999's multidimensional design [https://ethresear.ch/t/more-meters-or-more-prices-one-vs-multi-dimensional-fee-mechanisms-on-ethereum/26244]. Its strongest one-dimensional benchmark delivers 151.9M to 177.9M execution gas per block in simulation [https://ethresear.ch/t/more-meters-or-more-prices-one-vs-multi-dimensional-fee-mechanisms-on-ethereum/26244]. That benchmark produces 86.0 to 88.1 GiB a year of state growth, well short of the 120 GiB target, so capacity is left idle [https://ethresear.ch/t/more-meters-or-more-prices-one-vs-multi-dimensional-fee-mechanisms-on-ethereum/26244]. The paper finds that EIP-1559's update rule cannot push base fees low enough for high targets, and swaps in EIP-4844's exponential rule to test the alternative [https://ethresear.ch/t/more-meters-or-more-prices-one-vs-multi-dimensional-fee-mechanisms-on-ethereum/26244].

CULTURE

[CULTURE] Luke Dashjr accuses OCEAN of paying the miners' attacker.
Dashjr, who left OCEAN in August 2026 after a split over the BIP-110 fork, says the pool is "profiting from a cyberattack on their own customers, and rewarding the attackers" [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/]. He argues OCEAN could have stopped directing payouts to the address once the hijack was public [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/]. Critics replied that refusing to block an address is censorship resistance working as designed, and that Luxor is paying victims anyway [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/]. BeInCrypto notes that the dispute echoes the older Bitcoin argument over filtering transactions [https://beincrypto.com/bitcoin-miner-hack-ocean-pool-dashjr/].

[CULTURE] Molly White says crypto's midterm money mostly backed losers in close races.
White's 13 November 2026 analysis says Fairshake went 74 for 74 where its candidate was a clear or likely favourite, but 10 for 18 in competitive races [https://www.citationneeded.news/crypto-ai-lost-the-midterms/]. On her count, about half of the PAC's $154.5 million backed candidates who lost [https://www.citationneeded.news/crypto-ai-lost-the-midterms/]. She sets that against a Fairshake spokesman's claimed 92% success rate, which she calls the product of backing safe winners [https://www.citationneeded.news/crypto-ai-lost-the-midterms/]. Her conclusion that the PACs' influence in Congress has shrunk is her interpretation, not a measured legislative outcome [https://www.citationneeded.news/crypto-ai-lost-the-midterms/].

READING LIST

https://ocean.xyz/stats/bc1qphukp9rjfc4rcej7erpm9ae20xmtspw8pcddrr - OCEAN's own page for the attacker's address shows the hashrate spike and payouts.
https://github.com/BitGo/wallet-recovery-wizard/blob/master/NON_BITGO_RECOVERY.md - The documentation explains how two client keys move funds without the custodian.
https://ethresear.ch/t/elastic-ethereum/26236 - Kiraly's mainnet propagation numbers show how wide Ethereum's safety margin runs.
https://www.citationneeded.news/crypto-ai-lost-the-midterms/ - White's race-by-race tally is the basis for her argument about lost influence.

METHOD

Swept the masthead roster [https://raw.githubusercontent.com/openinterest-ai/paper/main/masthead/voices.csv], ethresear.ch, Citation Needed, Coin Center, exchange and custodian notices, Bitcoin chain data via mempool.space and trade reporting, covering the 48 hours ending 16 November 2026 at 09:00 UTC. Prior editions on the rehearsal page led with Hoodi, Binance, MEXC and Chainalysis; this lead is new [https://openinterest-ai.github.io/paper/rehearsal.html]. Cut for failed verification: a reported $3.76 million Kava Lend exploit, for which no primary or named secondary source was found, and early claims that the hijacker received nothing, which on-chain payouts contradict [https://mempool.space/address/bc1qphukp9rjfc4rcej7erpm9ae20xmtspw8pcddrr]. Claims resting on secondary sources, attributed by name: CoreX's 64,000-machine estimate, Hansen's and Dashjr's statements (BeInCrypto), the Coinone details (Bitcoin.com News), BitGo's statement (crypto.news), and the SEC totals (Lowenstein Sandler, as the SEC site refused automated access). X posts were cited through the reporting that embedded them because the xcancel mirror returned HTTP 451. Luxor's AI-attack attribution is unverified.

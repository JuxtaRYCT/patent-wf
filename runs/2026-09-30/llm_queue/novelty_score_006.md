# TASK novelty_score_006

## SYSTEM
You are a patent strategist and research scout for a bank's innovation lab. You score incoming research/news items for (a) genuine novelty of the core idea and (b) usefulness as raw material for new banking/finance inventions. Be harsh: incremental ML-on-finance papers score low on novelty. For non-finance items, extract the transferable MECHANISM (the abstract principle that could be moved into finance). For finance items, extract the OPEN PROBLEM.

## PROMPT
Score each item. Return one entry per id.

- id: arxiv:2609.32495
  pool: finance
  title: Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?
  abstract: An agent harness, the code that turns a model into an agent, writes its own record of each run, and that record is all a later reader gets when a run is disputed, investigated or audited. We call a record evidentiary when a reader who was not there can check it without trusting the writer. Across sixteen deployed frameworks, none writes one in full. Hearsay examines the record, not the task: five harnesses run fourteen tasks, three blinded LLM examiners and a human panel read the records, and every excerpt an examiner quotes is checked mechanically for who wrote it. First, the record lets a reader name the fault but not prove how the run went. Examiners name the right fault in 74 to 91% of 1
- id: arxiv:2609.21291
  pool: finance
  title: Efficient simulation schemes for pricing options under the Ornstein--Uhlenbeck driven stochastic volatility model
  abstract: We develop an efficient Monte Carlo simulation scheme for pricing options under the Ornstein-Uhlenbeck driven stochastic volatility model via the operator splitting approach. With an ingenious splitting of the governing stochastic differential equations, our operator splitting scheme admits analytic solutions in all sub-steps, so its implementation is simplified to require simulation of a few normal variates. This resolves the two typical numerical challenges in other simulation schemes, namely, sampling of conditional integrated variance and pathwise inverse integral transform of characteristic functions. There are three pioneering simulation schemes that attempt to overcome the above two n
- id: arxiv:2609.13961
  pool: finance
  title: Yet another asymptotic formula for implied volatility
  abstract: We derive a first-order representation of Black-Scholes implied variance in a continuous local martingale model. Total implied variance is the conditional expectation of the quadratic variation of the log price given its terminal value, up to a smaller-order term, for bounded standardized log-strikes. The framework incorporates small volatility-of-volatility, fast mean-reverting, and short-maturity asymptotics.
- id: arxiv:2609.14029
  pool: finance
  title: Special Markowitz: Thermodynamic Formalism for the Joint Regularisation of Returns and Covariance
  abstract: Special Markowitz (SM) regularises returns and covariance jointly, relative to a reference state (mu_ref, Sigma_ref). Each eigendirection of the whitened relative operator carries a signed spectral potential Phi_k, with persistence factor psi_k = exp(-Phi_k) > 0. Positive potentials attenuate empirical deviations from the reference geometry, zero potential preserves them, and negative potentials amplify them. The persistence factor psi_k governs both the return signal and the covariance deviation: the regularised deviation from the reference is psi_k times the empirical deviation. The logarithmic potential coordinate is characterised by a multiplicative composition law on the multiplicative 
- id: arxiv:2609.24548
  pool: finance
  title: Affine Volterra covariance processes and application to commodity markets
  abstract: We study affine stochastic Volterra equations on the cone of symmetric positive semidefinite matrices. For scalar kernels acting entrywise on the matrix dynamics, we establish weak existence by exploiting stochastic invariance results for Volterra equations on convex domains and derive a conditional Fourier--Laplace transform formula characterized by matrix-valued Riccati--Volterra equations. As an application, we extend the Gibson--Schwartz commodity model by replacing its variance-covariance structure with a Volterra--Wishart process. The resulting model allows for memory in the variances and for stochastic instantaneous correlation, while retaining affine tractability. Its joint Fourier--
- id: arxiv:2609.26445
  pool: finance
  title: A Practical Guide on Graphical Model Validation
  abstract: This manuscript formalizes the most popular model validation tools used in general insurance actuarial modeling. These include graphical tools like calibration plots, actual-vs-expected plots, lift charts, Murphy diagrams, as well as classical statistical tools such as Bregman losses, deviance losses, elementary losses, Murphy's decomposition and Gini scores. Particular emphasis is placed on whether calibration and discrimination are studied under a policy-weighted or an exposure-weighted population measure. This distinction is crucial in ensuring that premium schemes are calibrated on the correct scale.
- id: s2:c9629dc581d3f96447b2afc9dd5f3af2e68dfc1d
  pool: finance
  title: Improving quality assurance practices in the independent quality firm model for U.S. design-build projects
  abstract: Major transportation infrastructure projects in the U.S. using design-build delivery may adopt independent quality firms in which construction engineering and inspection (CEI) firms are retained by design-builders to perform quality assurance (QA) tasks that have traditionally been performed or overseen by public owners. This contractual shift can create ambiguity when technical QA, documentation/payment support and contract-compliance responsibilities are bundled within independent quality firm scopes. This study examines how experienced transportation professionals interpret independent quality firm (IQF) roles, stringency and independence, focusing on areas in which responsibility boundar
- id: arxiv:2609.26398
  pool: finance
  title: Weighted universal Value-at-Risk Superadditivity for discrete distributions
  abstract: The concept of weighted universal Value-at-Risk superadditivity (WUVS) was recently introduced by Chen et al. (2026) as a generalization of the question whether for some infinite mean distributions convex combinations of i.i.d. random variables can stochastically dominate the parent distribution. In this short note we prove that the property WUVS can basically never hold for discrete distributions except for the case of comonotonicity. This implies as a corollary that for discrete distributions with infinite mean it can also never hold that convex combinations of i.i.d. random variables can stochastically dominate the parent distribution. This settles an open problem mentioned in Müller (202
- id: arxiv:2608.17363
  pool: finance
  title: Conservation of Short-term Flows: Signed Optimal Transport
  abstract: This paper develops a theoretical framework for signed optimal transport. A global flatness measure induced by the continuum transport equation serves as the regularizer. We examine transport networks from a harmonic analysis perspective, prove the existence and uniqueness of the optimal coupling in the variational problem, and provide an algorithmic scheme that guarantees lossless information transport under bi-marginal constraints. To bridge theory with practice, we design an empirical analysis framework for the resulting optimal estimators, which is sufficiently general to accommodate both time-series and panel-structural analyses of the network, owing to the intrinsic invariance properti
- id: s2:a5743f0fc96fdc3185cb14e981b24c8e4b92c9a8
  pool: finance
  title: Will US Firms Adopt Stablecoins? Survey Says They're Not Enthusiastic
  abstract: We surveyed 148 firms active in the Fourth District about whether they had plans to use stablecoins. Responses were overwhelmingly negative, with only eight of our contacts expressing any such plans. Asked why they did not plan to use stablecoins, respondents cited satisfaction with existing payment methods, unfamiliarity with the new technology, and a lack of demand from clients and suppliers to pay using stablecoins.
- id: s2:03a4abda6bf2b1a1248b6eab4bd5ed7e0c236542
  pool: finance
  title: Development of an Web-Based Order Management System for Tailoring Businesses with Production Monitoring and WhatsApp Notifications
  abstract: Tailoring businesses, such as Anita Modiste Boutique, often face operational bottlenecks due to reliance on manual record-keeping for order processing and production monitoring, which leads to data inconsistencies, communication delays, and inefficient decision-making. This study proposes an integrated digital workflow model to modernize these operations, developed through the Rapid Application Development (RAD) methodology to ensure system alignment with administrative needs. The research contributes a novel approach by integrating customer order management, down payment tracking, and real-time internal coordination via an automated WhatsApp Gateway, serving as an active coordination mechan
- id: arxiv:2609.02381
  pool: finance
  title: Viscosity Supersolution Barriers to a Non-local Free Boundary Problem
  abstract: We study a parabolic obstacle partial integro-differential equation (PIDE) with a dynamically moving bilateral free boundary. This type of problem arises in the mathematical modeling of speculative asset bubbles with Lévy jump processes. We investigate the existence of viscosity supersolution barriers within the class of functions exhibiting linear asymptotic growth ($O(|g|)$ at infinity) across three distinct parametric regimes. Our intention is to determine when such a barrier can be constructed by analyzing the balance between the stabilizing local drift, defined by the discount rate $r$ and mean-reversion $ρ$, and the non-local jump dispersion, characterized by the large-jump intensity $
- id: s2:f4b51446c6e2597117ae185a6584c23690a1a5ac
  pool: finance
  title: Digitalisasi UMKM Bengkel melalui Sistem Booking Servis dan Monitoring secara Real-Time
  abstract: Digital transformation is increasingly important for micro, small, and medium enterprises (MSMEs), including vehicle repair workshops that still rely on manual registration, queue management, service records, and communication of repair progress. This study aims to design and implement a web-based service booking and real-time work monitoring system for workshop MSMEs. A qualitative research approach was applied using observation, interviews, literature review, and documentation. The system was developed iteratively using the Agile method and supports customer registration, service booking, customer and vehicle data management, reservation verification, mechanic work management, real-time st
- id: arxiv:2608.25877
  pool: finance
  title: A Hybrid Security Framework for Mini-Programs: Visual UI Compliance and Network Risk Assessment
  abstract: With the continuous development of the WeChat ecosystem, WeChat Mini Programs, due to their advantages of not requiring installation, using little memory, and being ready to use instantly, have seen a surge in user numbers and have now become an indispensable service carrier in mobile internet. However, as Mini Programs rapidly became popular, issues regarding the compliance of their interface interaction design and the safety of operational behavior have become increasingly apparent. Many Mini Programs have problems such as clickable buttons and icons not being standard in size, or ad pop-ups and payment entrances being placed in a way that is easy to misclick. The close or cancel buttons a
- id: arxiv:2609.08060
  pool: finance
  title: Pre-game paired-comparison modeling of professional League of Legends map outcomes
  abstract: We build and evaluate a pre-game win-probability forecaster for individual maps (``games'') in professional \emph{League of Legends} (LoL). The proposed model is a one-stage logistic regression fit end-to-end on the win/loss log-loss: each team's exponentially-weighted moving average of past same-side results, a ridge-shrunk stable strength that is the maximum-a-posteriori estimate of a logistic mixed model, and a first-pick draft covariate, natively calibrated out of sample (walk-forward slope $0.995$). It augments a purely dynamic Bradley--Terry specification with stable team strengths. A second, independently built two-stage composite mixed model under restricted maximum likelihood (REML)
- id: arxiv:2609.05047
  pool: finance
  title: Gatheral's Conjecture Revisited
  abstract: We consider the Heston model with perfect negative spot--variance correlation and its one-dimensional local-volatility projection. Let $I_T^{\mathrm H}$ and $I_T^{\mathrm{LV}}$ denote their respective integrated variances over $[0,T]$. We establish the inequality \[ \mathbb{E}\bigl[(I_T^{\mathrm H}-K)^+\bigr] 0$ and every strike $K>0$. Consequently, Heston integrated variance is strictly smaller in convex order than the integrated variance of the calibrated local-volatility model. This strict ordering gives a Heston-model counterexample to the convex-order inequality conjectured by J. Gatheral.
- id: s2:1e87784a9c0fc52b47849cab73cc4e9b600c8409
  pool: finance
  title: A matter of credible guarantee: the EU’s Global Gateway initiative and the European Investment Bank’s role in development finance
  abstract: ABSTRACT The European Investment Bank (EIB) has become the single largest institutional investor and a primary implementing partner of the European Union’s (EU’s) Global Gateway (GG) initiative. Yet the EIB has also long been a risk-averse financial institution, focused upon defending its Triple-A credit rating and lending principally within the EU. Prior to the 2020s, the EIB never referred to itself as a development bank. How then is the bank’s important role in the GG and increased international development lending to be best understood? What implications does this role and increased lending have for its relationship with the European Commission? Applying elements of historical institutio
- id: s2:aa4e957ff2bc8d3f3d927a364bfc196b8b6a0acf
  pool: finance
  title: A Novel Computational Framework for Annuity Interest Rate Determination: Beyond Traditional Interpolation Methods
  abstract: Aims: This study aims to develop a computationally efficient mathematical framework for determining the periodic interest rate in annuity contracts, thereby addressing the limitations of traditional tabular interpolation methods. Study Design: The study employs mathematical derivation and numerical analysis to formulate the annuity interest rate problem as a root-finding exercise and implements the Newton-Raphson method with strategic initialisation and rigorous error quantification. Place and Duration of Study: Department of Basic Sciences, School of General Studies, Auchi Polytechnic, Auchi, Edo State, Nigeria, between December 2025 and July 2026. Methodology: The research derives the impl
- id: arxiv:2608.29468
  pool: finance
  title: The Convergence Rate of Stochastic Tracking with Application to Optimal Execution
  abstract: We study the quadratic tracking problem of a general stochastic target process with absolutely continuous controls, with and without terminal constraint. We derive explicit, non-asymptotic upper bounds in terms of a Besov-type modulus of the target. These bounds yield sharp explicit rates that specialize to the square-root order for semimartingale targets. We then apply these results to a generalized Obizhaeva--Wang execution model with random terminal inventory. We first develop a Hilbert-space approach to characterize its optimal strategy, which includes jumps. To avoid such trading spikes, one regularizes the problem by a quadratic trading-rate penalty with coefficient $\varepsilon$. We t
- id: s2:e93f259f9b202d99b3fcc66307f478c435f634b6
  pool: finance
  title: Legal Regulation of Banking Activities in Ethiopia
  abstract: The article analyzes the formation and development of legal regulation of banking activities in Ethiopia. Special attention is paid to the recent reforms in the legal regulation of Ethiopia’s banking sector. The article concludes that in carrying out banking regulation and supervision, the National Bank of Ethiopia places particular emphasis on the stability of banks and the protection of depositors’ rights. Recent banking reforms have opened the door for foreign investors to participate in Ethiopia’s banking sector. Significant market-oriented changes have taken place in the area of currency regulation. Free economic zones are being established and developed in Ethiopia. A distinctive featu
- id: arxiv:2608.23393
  pool: finance
  title: KellyBoost: Growth-Optimal Portfolio Construction with Gradient-Boosted Trees
  abstract: KellyBoost is a single multi-output XGBoost model whose softmax output is the portfolio: with y the vector of per-asset holding-period returns, the training loss is - log(1 + w y), the negative log growth rate, so the fitted model is the growth-optimal (Kelly) allocation conditioned on the features. The objective is exact rather than a surrogate: we derive the gradient, the analytic diagonal Hessian and the full Hessian in closed form, verify them by finite differences, and ship a dependency-free reference engine.
- id: arxiv:2609.08959
  pool: finance
  title: The Delta of a Variance Swap
  abstract: We define the variance swap delta as the sensitivity of the price of variance to a change in underlying price. We use Carr-Madan spanning formulas to analyze this sensitivity when the implied volatility smile curve may depend on the underlying price. We show that the variance swap total delta is zero for the class of smile curves that are pure functions of (log) moneyness, which goes against the empirical observation that variance is up when the market is down. We propose a simple modification of the smile to correct this issue.
- id: s2:9ee80236d26edd0135165558c73de0a4995db3f3
  pool: finance
  title: Perancangan Sistem Pencatatan Kas Berbasis Cash Advance Pada Transaksi Pembelian Biji Kakao Di Pt Pesona Agri Khatulistiwa
  abstract: Cash recording for cocoa bean purchase transactions at PT Pesona Agri Khatulistiwa is still done manually using Microsoft Excel, resulting in challenges such as non-real-time recording, payment calculation errors, difficulties in reconciling transactions with cash advance balances, delays in fund disbursement, and unstructured recording of debts owed to farmers. This study aims to design a cash advance-based cash recording system that integrates fund management, purchase realization recording, and inventory information as supporting data. The study employs a descriptive qualitative approach with data collection through observation, interviews, and document analysis. System development uses t
- id: arxiv:2609.07351
  pool: finance
  title: Fixed Points for the $q$-Bass Martingale: Existence, Stability, and Convergence
  abstract: We establish existence, uniqueness, stability, and convergence results for one-dimensional $q$-Bass martingales, characterized as the martingales with prescribed initial and terminal marginals whose transition kernels are closest to a reference measure $q$. Their existence is equivalent to the solvability of a fixed-point problem for probability distributions. Building on Acciaio and Marini (2026), that requires the first marginal to be supported on finitely many points, we study the case of general marginals in convex order. Under the assumption that $q\llλ$, we prove existence, uniqueness and stability of fixed-point distributions, $\mathcal{W}_\infty$-convergence of the fixed-point iterat
- id: arxiv:2609.29975
  pool: finance
  title: Sluice: Global Invariant, Local Enforcement for Pooled Payment-Channel Liquidity
  abstract: A routing node on the Lightning Network holds its liquidity in separate channels, so a payment can fail at a channel whose outbound balance is exhausted while the node's other channels still hold balance. Pooling the channels into one reserve fixes this only if the node's draws across all channels stay within the reserve: a global invariant that each counterparty must enforce from its own channel, with no shared counter that off-chain draws can update. A node must therefore split the reserve into per-channel quotas in advance or coordinate every draw with every counterparty. On three Lightning snapshots the advance split forfeits $16$ to $67\%$ of the pooling gain over unpooled channels, and
- id: arxiv:2609.17316
  pool: finance
  title: Can We Stop The Ads? Taxonomy and Characterization of Smartphone Splash Ads and Existing Countermeasures
  abstract: Splash ads are full-screen advertisements that pop up and appear as the first interaction page when users start an app, often tricking users into unknowingly activating certain trigger mechanisms, such as moving the phone to redirect users to other profit-driven third parties. So far, splash ads have already caused significant real-world impacts, ranging from significantly delaying emergency response to distracting drivers, as well as degrading accessibility of apps to vision-impaired users. We analyze 108 documented implementations of advertising defenses to examine their applicability to splash ads and the requirements users face when deploying them. Our analysis identifies substantial dep
- id: s2:499f658875e94b33b52eef1d6c25d3614a313ecc
  pool: finance
  title: Implementasi Website Pembayaran Rusunawa pada Dinas Perumahan dan Kawasan Permukiman (Disperkim) Kota Tegal
  abstract: This research addresses the inefficiency of manual payment administration at the Tegal City Housing and Settlement Agency (Disperkim) by developing an integrated Rental Apartment (Rusunawa) Payment Website to enhance data management effectiveness. The study utilized the Waterfall method, encompassing requirements analysis, system design, implementation, testing, and maintenance. Built using the Laravel framework, PHP, and MySQL, the platform establishes two distinct user access roles: tenants—who can view bills, complete payments, and access payment history—and administrators, who manage block, tenant, billing, and payment data while overseeing monitoring and reporting. Black-box testing acr
- id: arxiv:2608.22864
  pool: finance
  title: From Exponential to Polynomial: An Exact Filter for High-Dimensional MSM Models
  abstract: In this paper we propose a new formulation of the Bayesian Filter as used in the discrete-time Markov-Switching-Multifractal (MSM) model of volatility based on existing permutation symmetry within the likelihood structure. We show both analytically and empirically that such a formulation leads to a reduction in time complexity from $O(D^k)$ to $O(k^D)$ thereby significantly reducing the computational bottleneck associated with dimensionality. We compare the agreement between the naive and sector filters and find that while there are significant disagreements, the ground-truth recovery of the latter seems to improve on the former.
- id: s2:517b8fdfb6eb9970a1c031421ba4261101671045
  pool: finance
  title: Impact of the volume-based procurement for intraocular lenses combined with the diagnosis-related group’s payment reform on hospitalization costs and expenditure structure among cataract patients: an interrupted time series analysis
  abstract: Background Cataract surgery is one of the most resource-intensive procedures in China, with intraocular lens (IOL) costs accounting for a substantial proportion of total hospitalization expenditure. To address persistently high prices of high-value medical consumables, our hospital implemented the Beijing-Tianjin-Hebei “3 + N” regional alliance procurement for IOLs in January 2022, followed by DRG payment reform in January 2024. However, the synergistic effects of these two sequential policies on cataract surgery costs—particularly on both cost levels and expenditure composition—have not been systematically evaluated. Methods We conducted a retrospective analysis of 8,458 cataract patients w
- id: arxiv:2609.21271
  pool: finance
  title: Nested Clustered Optimization Is One End of a Schur Bridge, and the Interior Is Sometimes Provably Better
  abstract: Nested clustered optimization allocates within each cluster from the cluster's own covariance block and then across the resulting cluster portfolios. Block inversion says the unconstrained minimum-variance portfolio has the same two-tier shape, with each block replaced by its Schur complement against every other asset. Conditioning instead on one knot from each other cluster truncates the conditioning set in the manner of a Vecchia approximation, and we give the rank-one model of cross-cluster dependence under which it is exact. Damping the complement by $γ\in[0,1]$ then gives a bridge with nested clustered optimization at $γ=0$ and the global optimum at $γ=1$, with no linear solve larger th

## OUTPUT JSON SCHEMA
```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "scores"
 ],
 "properties": {
  "scores": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "id",
     "novelty",
     "usefulness",
     "mechanism_or_problem",
     "tags"
    ],
    "properties": {
     "id": {
      "type": "string"
     },
     "novelty": {
      "type": "integer",
      "description": "1-10 novelty of the core idea"
     },
     "usefulness": {
      "type": "integer",
      "description": "1-10 value as input for finance inventions"
     },
     "mechanism_or_problem": {
      "type": "string",
      "description": "<=30 words"
     },
     "tags": {
      "type": "array",
      "items": {
       "type": "string"
      }
     }
    }
   }
  }
 }
}
```

Write the answer to: runs/2026-09-30/llm_responses/novelty_score_006.json

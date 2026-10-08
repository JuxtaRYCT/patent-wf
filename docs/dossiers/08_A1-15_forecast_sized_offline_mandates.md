# #8 · A1-15 — Forecast-sized offline mandates for machine and agent payments

| | |
|---|---|
| **Origin** | Approach 1 bisociation: *Mastercard helps Danske Bank with Denmark-first agentic transaction* (PYMNTS) × *Reading the Sky to Forecast the Ground: Physics-Informed Link-State Forecasting for LEO Networks* (arXiv 2609.26696). Context: Mastercard *Agent Pay for Machines* (Jun 2026). |
| **Domain** | Machine-to-machine and agent payments, offline payments / offline CBDC |
| **Scores** | final **6.34** · novelty 7 · utility 6 · crazy 7 |
| **Verdict** | **Refine.** The deep check found only static, manually configured offline limits |

## 1. Problem, framed technically
Autonomous payers (EVs paying for charging and tolls, drones, ships, agricultural and remote IoT, rural field agents) lose connectivity along predictable but varying stretches. Offline payment credentials today use **fixed limits and fixed expiries**, configured in advance: Square, Toast and Nexi terminals default to limits like £100 and 24-hour upload windows. Limits set too high create double-spend and fraud exposure; limits set too low strand the machine.

## 2. The invention
1. **Mission and route input.** A planned route or mission profile (timeline × location).
2. **Connectivity-gap forecast.** A physics-informed forecaster predicts gaps with confidence intervals from satellite-constellation geometry (TLE ephemerides), weather attenuation, terrestrial coverage maps and historical outage traces.
3. **Consumption forecast.** Expected spend during each gap (charging, tolls, parking, data purchases), with quantiles.
4. **Credential shaping.** For each gap the issuer provisions an offline credential: a pre-authorised token bundle, an offline CBDC purse, or EMV offline authority. Its **value cap** is a high quantile of spend plus a margin, its **validity window** runs from gap start minus δ to forecast reconnection plus tolerance, and it is **geofenced** to the forecast corridor, optionally restricted to certain merchant categories. The secure element enforces all constraints offline.
5. **Reconciliation and learning.** On reconnection, spend is reconciled, unused value is reclaimed, and the forecaster is updated with the realised gaps.

### Technical effect / evidence
Offline exposure (value × time outstanding) at equal payment-success rate, compared with fixed-limit baselines. Failed-payment rate in gaps.

## 3. Prior art and differences
| Reference | Discloses | Does **not** disclose |
|---|---|---|
| Offline terminal modes (Square, Toast, Nexi docs) | Static per-transaction limits and fixed upload windows | Forecast-sized, time- and geo-bounded credentials |
| Fluency offline CBDC protocol US11935065B2 | Offline CBDC participation via collateral chains | Connectivity-forecast sizing |
| Nymi/Bionym pre-authorised wearable US20150206364A1 | A pre-authorised biometric device | Forecast-based credential shaping |
| Gnomon (arXiv 2609.26696) | LEO link-state forecasting | Any payment use |

## 4. Draft claims
**Claim 1.** A method comprising: receiving a planned trajectory of an autonomous payer device; forecasting, from orbital, weather and coverage data, time intervals during which the device will lack network connectivity along the trajectory; forecasting a payment demand of the device during each interval; provisioning to a secure element of the device an offline payment credential whose value limit, validity window and geographic scope are determined from the forecast interval and payment demand; enforcing the limit, window and scope by the secure element during offline operation; and reconciling offline payments upon reconnection.
**Dependent:** value limit = demand quantile + margin · validity from forecast gap start minus δ to reconnection plus tolerance · a geofence polygon along the forecast corridor · merchant-category restriction · learning from realised gaps · offline CBDC purse embodiment · agent-platform embodiment for software agents running on intermittently connected devices.

## 5. Eligibility
Secure-element enforcement and credential provisioning driven by a physical-channel forecast give a clear technical effect in all three jurisdictions.

## 6. Commercial path
Card networks' machine-payment programmes, EV charging networks, automotive OEM wallets, and CBDC offline pilots (RBI e₹ offline, digital euro offline).

## 7. PoC (4 weeks)
Public TLE data plus coverage maps, then a gap forecaster, then a credential shaper in a simulated SE. Compare exposure and failures against static limits on synthetic routes.

## 8. Risks
Forecast error; handled with margins and fallbacks. Standards alignment (EMV and CBDC offline specs).

# DC5 mock dataset — source definitions

> **Blind dataset.** This directory is the answer key for the DC5 mock dataset. It should not be shared with the COSI team or the community until the data challenge is unblinded.

The DC5 mock dataset starts from the DC4 mock dataset (3 months, same orbit, orientation and backgrounds) and changes the source content:

| | DC4 components (non-GRB) | Fraction |
|---|---|---|
| Reused (same source files; 2 of these carry only the Request 3 bug fix) | 27 | 51% |
| Modified | 21 | 40% |
| Removed | 5 | 9% |
| **New** (relative to the ~71 DC4 components) | 17 | 24% |
| GRBs (unchanged, as requested) | 18 | |

DC5 therefore has 65 non-GRB components plus 18 GRBs.

**How the split was made.** Components that belong to one physical source (e.g. line + continuum maps, flare + quiescent states, the three nova components) were grouped, and the groups were shuffled with a random seed (3891814211, recorded in `DC5_draw.json`). Groups were assigned to *removed* (≈10% of files, only from sources that are not well-known detections: the Crab, Cyg X-1/X-3, Cen A, NGC 4151, the 511 keV bulge/disk, Galactic 26Al/60Fe, Cas A, etc. were protected), then *modified* (≈40%), with the rest *reused*. The modification applied to each drawn source was then chosen by hand from the literature (alternative library model where one exists, otherwise a simple flux/width/state change within the published range). Positions of the arbitrary new sources are drawn from the same seed. Running `scripts/draw_dc5.py` without a seed gives a different realisation.

Files:
- `DC5_mock_dataset_src_list.txt` — the `src_list` for cosi-sim (82 entries; checked with `Setup.setup_srcs()`).
- `DC5_mock_dataset_manifest.md` — every component with its status, source path and what to do (simulate / re-simulate / reuse the existing DC3/DC4 event file).
- `DC5_build_log.json`, `DC5_draw.json` — machine-readable record of the draw and of every change.
- `scripts/` — `draw_dc5.py` (random split), `build_dc5.py` (writes `sources/` for this draw), `mapflux.py` (integrates cosima 3D maps), `eq2gal.py` (RA/Dec → l, b).
- `sources/` — one directory per modified, bug-fixed or new source, each with a `README_DC5.md` describing the model, the change, and references.

## Reused sources (same source files)
| DC4 mock component | cosi-sim source path | Action |
|---|---|---|
| CasAG16distribution | `DC4/sources/Nucleosynthesis/CasAG16distribution` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/CasAG16distribution_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Positrons_Central_Source | `DC4/sources/511/Positrons_Central_Source` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/Positrons_Central_Source_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| positrons_thin_disk_cont | `DC4/sources/511/Positrons_Thin_Disk_cont` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/positrons_thin_disk_cont_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| positrons_thin_disk_line | `DC4/sources/511/Positrons_Thin_Disk_line` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/positrons_thin_disk_line_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| SN1987A | `DC4/sources/Nucleosynthesis/SN1987A` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/SN1987A_unbinned_data_filtered_with_SAAcut.fits.gz |
| VelaJr_44Ti | `DC4/sources/Nucleosynthesis/VelaJr_44Ti` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/VelaJr_44Ti_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Virgo_511 | `(no library file)` | reuse DC4 event file COSI-SMEX/DC4/Data/Sources/Virgo_511_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| NGC_1068 | `DC4/sources/Extragalactic/NGC_1068` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/NGC_1068_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| 4C71p07 | `DC4/sources/Extragalactic/4C71p07` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/4C71p07_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| 3C454p3_low | `DC4/sources/Extragalactic/3C454p3_low` | re-simulate with the same source file (light-curve bug) |
| 3C454p3_high | `DC4/sources/Extragalactic/3C454p3_high` | re-simulate with the same source file (light-curve bug) |
| CenA | `DC4/sources/Extragalactic/CenA` | reuse DC4/DC3 event file COSI-SMEX/DC4/Data/Sources/CenA_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Crab_DC4 | `DC4/sources/Galactic/Crab` | re-simulate with the same source file (light-curve bug) |
| Globular_Cluster_Tuc_47 | `DC3/sources/511/Globular_Cluster_Tuc_47` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Globular_Cluster_Tuc_47_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Globular_Cluster_Omega_Cen | `DC3/sources/511/Globular_Cluster_Omega_Cen` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Globular_Cluster_Omega_Cen_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Globular_Cluster_NGC_6397 | `DC3/sources/511/Globular_Cluster_NGC_6397` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Globular_Cluster_NGC_6397_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Globular_Cluster_NGC_6121 | `DC3/sources/511/Globular_Cluster_NGC_6121` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Globular_Cluster_NGC_6121_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Positrons_from_26Al_line | `DC3/sources/511/Positrons_from_26Al_line` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Positrons_from_26Al_line_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Positrons_from_26Al_cont | `DC3/sources/511/Positrons_from_26Al_cont` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Positrons_from_26Al_cont_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Positrons_from_44Ti_line | `DC3/sources/511/Positrons_from_44Ti_line` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Positrons_from_44Ti_line_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Positrons_from_44Ti_cont | `DC3/sources/511/Positrons_from_44Ti_cont` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/Positrons_from_44Ti_cont_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| PSRB1259 | `DC3/sources/Galactic/PSRB1259` | re-simulate with the same source file (light-curve bug) |
| LS5039 | `DC3/sources/Galactic/LS5039` | re-simulate with the same source file (light-curve bug) |
| 26Al_NE2001 | `DC3/sources/Al26/26Al_NE2001` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/26Al_NE2001_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| 60Fe_Cyg_Region | `DC3/sources/Fe60/60Fe_Cyg_Region` | reuse DC4/DC3 event file COSI-SMEX/DC3/Data/Sources/60Fe_Cyg_Region_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| Narrow_Bulge_511 | `DC5/sources/511/NB_511` | re-simulate (511 keV map bug fixed) |
| Vela_SNR_511 | `DC5/sources/511/Vela_SNR_511` | re-simulate (511 keV map bug fixed) |

## Modified sources
| DC4 mock component | DC5 source path | Modification |
|---|---|---|
| cygX3 | `DC5/sources/Galactic/cygX3` | transition state replaced by the hypersoft state (DC3 Cangemi et al. 2021 models) for the full 3 months at nominal flux 0.001233 ph/cm2/s |
| positron_annihilation_in_flight | `DC5/sources/511/Positrons_In_Flight_Annihilation` | Orientation 'Galactic Fixed -1.4 -0.2' -> 'Galactic Fixed -0.2 -1.4' (bug fix: MEGAlib order is b, l); flux 0.00031 -> 0.000372 ph/cm2/s (x1.2) |
| Tycho | `DC5/sources/Nucleosynthesis/Tycho` | flux 1.6e-05 -> 1e-05 ph/cm2/s (1.0x instead of 1.6x the Lopez et al. 2015 upper limit) |
| USco | `DC5/sources/Nucleosynthesis/USco` | 60Fe line fluxes 4.5e-05 -> 2.25e-05 ph/cm2/s each (x0.5; 60Fe/26Al per line 0.75 -> 0.375); 26Al unchanged |
| LMC_511 | `DC5/sources/511/LMC_511` | DC4 LMC_511 model replaced by the alternative DC3 LMC_Gaussian_511 definition, with flux x2 relative to DC3 (4.27e-06 -> 8.54e-06 ph/cm2/s; still below the SPI 2-sigma limit 3.6e-5, Siegert et al. 2016) |
| M31_511 | `DC5/sources/511/M31_511` | DC4 M31_511 model replaced by the alternative DC3 M31_Gaussian_511 definition, with the Gaussian width reduced 1.0 -> 0.5 deg (emission concentrated in the M31 bulge); DC3 flux 2.13e-7 ph/cm2/s |
| NGC_4151 | `DC5/sources/Extragalactic/NGC_4151` | thermal (Gamma=1.75, Ecut=200 keV) normalisation x1.5 (brighter state, Lubinski et al. 2010); non-thermal tail unchanged; flux 0.00188 -> 0.002726 ph/cm2/s |
| 1RXSJ170849 | `DC5/sources/Galactic/1RXSJ170849` | flux 0.00033 -> 0.000247 ph/cm2/s (x0.75, long-term hard X-ray variability, den Hartog et al. 2008) |
| magnetar2 | `DC5/sources/Galactic/magnetar2` | flux 0.00033 -> 0.000495 ph/cm2/s (x1.5) |
| Broad_Bulge_511 | `DC5/sources/511/BB_511` | 511 keV side nodes set to zero (bug fix) and broad-bulge intensity scaled x0.85; integrated flux 1.480e-03 -> 6.290e-04 ph/cm2/s |
| nova_co_511keV | `DC5/sources/Galactic/nova_co_511keV` | flux 0.01537 -> 0.02305 ph/cm2/s (x1.5: nova at 0.82 kpc instead of 1 kpc) |
| nova_co_continuum | `DC5/sources/Galactic/nova_co_continuum` | flux 0.1221 -> 0.1831 ph/cm2/s (x1.5: nova at 0.82 kpc instead of 1 kpc) |
| nova_co_478keV | `DC5/sources/Galactic/nova_co_478keV` | flux 2.044e-06 -> 3.066e-06 ph/cm2/s (x1.5: nova at 0.82 kpc instead of 1 kpc) |
| 4C21p35_noflare | `DC5/sources/Extragalactic/4C21p35_noflare` | flux 0.0005535 -> 0.0008302 ph/cm2/s (x1.5) |
| 4C21p35_flare | `DC5/sources/Extragalactic/4C21p35_flare` | flux 0.01729 -> 0.02594 ph/cm2/s (x1.5) |
| 1E1740_compow | `DC5/sources/Galactic/1E1740_twocompt` | swapped compow model for the alternative twocompt model (Bouchet et al. 2009) |
| cygX1_hard | `DC5/sources/Galactic/cygX1_soft` | source in the soft state for the full 3 months (Cangemi et al. 2021 model) |
| GRS1758 | `DC5/sources/Galactic/GRS1758` | flux 0.003495 -> 0.002621 ph/cm2/s (x0.75, dimmer hard-state epoch) |
| MAXIJ1820 | `DC5/sources/Galactic/MAXIJ1820` | MAXIJ1820_0p1-0p4: 0.1382 -> 0.09675; MAXIJ1820_0p4-10: 0.005964 -> 0.004174 ph/cm2/s (x0.7, fainter hard-state outburst) |
| 26Al_Cyg_Region | `DC5/sources/Nucleosynthesis/26Al_Cyg_Region` | Gaussian width 3.0 -> 4.5 deg (Martin et al. 2009: 3 deg is a lower limit, +-3 deg uncertainty); flux unchanged |
| 60Fe_NE2001 | `DC5/sources/Nucleosynthesis/60Fe_NE2001` | map intensity x0.65 (60Fe mass 3.5 -> 2.3 Msun); total flux (both lines) 2.997e-04 -> 1.948e-04 ph/cm2/s |

## Removed sources
| DC4 mock component |
|---|
| GS1903 |
| Kepler |
| OrEr |
| PSRJ1846 |
| MAXIJ1348 |

## New sources
| Name | Origin | Position | Model |
|---|---|---|---|
| 3C273 | (from DC2) |  | average state (Madsen et al. 2015), flux 8.6e-4 ph/cm2/s; DC2 transmission-probability line replaced by DC3+ settings |
| 3C279_high | (from DC3) |  | high-state spectrum at its physical flux (x1 instead of x100): 1.19e-4 ph/cm2/s, 19.6% polarisation at 45 deg |
| PSRB1509 | (from DC2) |  | 3 energy bands with periodic pulse profiles (Kuiper et al. 2015); DC2 transmission-probability lines replaced by DC3+ settings |
| NGC_4945 | (literature) | l=305.2721, b=13.3397 | cutoff power law Gamma=1.9, Ecut=300 keV (NuSTAR: Ecut > 200-300 keV, Puccetti et al. 2014); F(20-100 keV)=2.0e-10 erg/cm2/s |
| IC_4329A | (literature) | l=317.4963, b=30.92 | cutoff power law Gamma=1.70, Ecut=178 keV, F(5-79 keV)=3.04e-10 erg/cm2/s (Brenneman et al. 2014) |
| GX339m4_hard | (literature) | l=338.9391, b=-4.3265 | black-hole LMXB in a moderately bright hard state for the full 3 months: Gamma=1.6, Ecut=200 keV, F(20-200 keV)=1.5e-9 erg/cm2/s; 5% polarisation |
| 4U0142p61 | (literature) | l=129.384, b=-0.4307 | log-parabola, local index 0.93 at 50 keV with the nuFnu peak at 228 keV (beta=0.353); F(20-229 keV)=1.5e-10 erg/cm2/s (den Hartog et al. 2008); steady (no pulsation light curve) |
| 26Al_Carina_Region | (literature) | l=287.6, b=-0.6 | 1809 keV line, 2 deg Gaussian at Trumpler 16, flux 1.5e-5 ph/cm2/s (Voss et al. 2012), width as DC3 Cygnus model |
| Ti44_hidden_SNR | (arbitrary) | l=300.398, b=-0.163 | unknown young, dust-obscured SNR: point-like 44Ti line, 4000 km/s broadening, 1.2e-5 ph/cm2/s (comparable to Tycho/Kepler models) |
| nova_one_22Na | (arbitrary) | l=71.159, b=4.096 | ONe nova at 1.5 kpc: 22Na 1275 keV line (~20 keV FWHM), ~1e-5 ph/cm2/s at 1 kpc (Hernanz 2014) scaled to 1.5 kpc; constant (22Na lifetime 3.75 yr) |
| Positrons_Point_Source | (arbitrary) | l=55.505, b=1.707 | steady point-like 511 keV line (e.g. a microquasar or pulsar positron source), 2.5e-5 ph/cm2/s, same line width as the DC4 central source |
| BHXB_hard_transient | (arbitrary) | l=15.756, b=0.966 | new black-hole X-ray binary in a long hard-state outburst: Gamma=1.6, Ecut=150 keV, 1.5e-3 ph/cm2/s (about 1/20 of the Crab in 100 keV-10 MeV) |
| PWN_hard_source | (arbitrary) | l=349.231, b=0.547 | Crab-like pulsar wind nebula ~80x fainter than the Crab nebula: power law Gamma=2.1, 4e-4 ph/cm2/s, 30% polarisation |
| magnetar3 | (arbitrary) | l=199.713, b=0.009 | steady hard-tail magnetar (no pulsation light curve): log-parabola alpha=1.2, beta=0.30, pivot 143 keV, 2.5e-4 ph/cm2/s, 50% polarisation |
| MeV_blazar | (arbitrary) | l=330.525, b=-30.528 | high-redshift FSRQ with nuFnu peak at 1 MeV: log-parabola alpha=2.0, beta=0.2 at 1 MeV, 3e-4 ph/cm2/s (between 4C 71.07 and 3C 279), 15% polarisation |
| Seyfert_new | (arbitrary) | l=31.746, b=-21.833 | Seyfert galaxy with Gamma=1.8, Ecut=300 keV, 3e-4 ph/cm2/s (a few times fainter than NGC 4151) |
| 26Al_new_region | (arbitrary) | l=316.177, b=-0.02 | additional massive-star region: 4 deg Gaussian 1809 keV source, 1.5e-5 ph/cm2/s (similar to Carina / ~40% of Cygnus) |

## GRBs (unchanged)
| Component | Source path | Action |
|---|---|---|
| GRB_bn081207680 | `DC3/sources/GRBs/bn081207680` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn081207680_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn090424592 | `DC3/sources/GRBs/bn090424592` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn090424592_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn100612726 | `DC3/sources/GRBs/bn100612726` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn100612726_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn110605183 | `DC3/sources/GRBs/bn110605183` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn110605183_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn131122490 | `DC3/sources/GRBs/bn131122490` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn131122490_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn140329295 | `DC3/sources/GRBs/bn140329295` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn140329295_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn161004964 | `DC3/sources/GRBs/bn161004964` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn161004964_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn170405777 | `DC3/sources/GRBs/bn170405777` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn170405777_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn180504136 | `DC3/sources/GRBs/bn180504136` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn180504136_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn180703876 | `DC3/sources/GRBs/bn180703876` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn180703876_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_bn080802386_flux150 | `DC3/sources/GRBs/bn080802386` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_bn080802386_flux150_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_MGF051103 | `DC3/sources/GRBs/MGF051103` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_MGF051103_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_MGF070201 | `DC3/sources/GRBs/MGF070201` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_MGF070201_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_MGF070222 | `DC3/sources/GRBs/MGF070222` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_MGF070222_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_MGF180128A | `DC3/sources/GRBs/MGF180128A` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_MGF180128A_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_MGF200415A | `DC3/sources/GRBs/MGF200415A` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_MGF200415A_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| GRB_MGF231115A | `DC3/sources/GRBs/MGF231115A` | reuse DC3 event file COSI-SMEX/DC3/Data/Sources/GRB_MGF231115A_3months_unbinned_data_filtered_with_SAAcut.fits.gz |
| MgtBurst_bright_complex | `DC3/sources/GRBs/MgtBurst_bright_complex` | reuse DC4 event file COSI-SMEX/DC4/Data/Sources/MgtBurst_bright_complex_unbinned_data_filtered_with_SAAcut.fits.gz (uses a light curve: check against the light-curve bug) |

## Request 2 — DC4 mock sources (non-GRB) with a light curve
These must be re-simulated once the light-curve bug is fixed: Crab (P1, bridge, P2), 1RXSJ170849, magnetar2, 3C454p3_low, 3C454p3_high, nova_co_511keV, nova_co_continuum, nova_co_478keV, 4C21p35_noflare, 4C21p35_flare, PSRB1259, LS5039, PSRJ1846, MAXIJ1820, MAXIJ1348 (16 files). MgtBurst_bright_complex (GRB directory) also uses a light curve. In DC5, PSRJ1846 and MAXIJ1348 are removed; the new PSRB1509 also uses (periodic) light curves.

## Request 3 — bug fixes and verification
**In-flight annihilation position.** `DC5/sources/511/Positrons_In_Flight_Annihilation` now declares `Galactic Fixed -0.2 -1.4`. MEGAlib reads Galactic Fixed as (b, l): every other library source follows this order, e.g. the Crab `-5.78434 184.5575` (l = 184.56°, b = −5.78°, recomputed independently from RA/Dec with `scripts/eq2gal.py`), the LMC `-32.89 280.46` and Kepler `6.8 4.5`. The source is therefore centred at (l, b) = (−1.4°, −0.2°) as intended. The final check is a short cosima run (a few minutes on one core) imaged with mimrec; this was not possible here because MEGAlib is not installed in this environment.

**511 keV line maps.** The 510 and 512 keV nodes were set to zero, so the linearly interpolated line contains exactly the 511 keV node value per keV. Integrated fluxes (from `scripts/mapflux.py`):

| Map | Before | After fix | Note |
|---|---|---|---|
| NB_511 | 5.60e-4 | 2.80e-4 | |
| BB_511 | 1.48e-3 | 7.40e-4 | DC5 additionally scales BB by 0.85 → 6.29e-4 |
| Vela_SNR_511 | 7.03e-4 | 3.52e-4 | matches the 3.5e-4 in its README |

With the fix alone, narrow + broad bulge + DC4 central source = 2.80e-4 + 7.40e-4 + 0.80e-4 = 1.10e-3 ph cm⁻² s⁻¹, i.e. the intended ≈1.09e-3. In DC5 (BB × 0.85) the bulge total is 9.9e-4, within 1σ of the SPI bulge value. The DC3 originals were left untouched as the record of what was simulated for DC3/DC4.

## Notes
- **LMC_511, M31_511, Virgo_511:** the DC4 definitions were simulated outside cosi-sim and differ from the DC3 `*_Gaussian_511` files. Virgo_511 (reused) reuses the DC4 event file directly. LMC_511 and M31_511 (modified) are replaced by the alternative DC3 Gaussian definitions plus a small additional change, documented in their READMEs.
- Several DC4 maps and light curves are stored as `.dat.gz` in cosi-sim (thin-disk maps, magnetar light curves, including the copies in DC5/sources/Galactic/1RXSJ170849 and magnetar2). As for DC4, gunzip them in place before running the pipeline. All other DC5 files are used as-is.
- Science-team inputs (due Nov 15) will be added as a follow-up to this directory.

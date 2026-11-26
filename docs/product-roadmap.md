# Mativio — Product roadmap

The long-term goal is a **full digital property management system** for the family's buildings: a public showcase for prospective tenants, and an owner dashboard and tenant portal for rent, renewals, maintenance, tenant requests with SLAs, and CCTV health.

Status legend: ✅ done (on the development branch) · 🟡 waiting on the owner · ⬜ not started.

## Phase 1 — Ready for real tenants (current)

| # | Item | Status |
|---|---|---|
| 1 | Public site: home, properties, details, localities, story, contact, legal | ✅ |
| 2 | Availability statuses with status-based actions | ✅ |
| 3 | Shareable link and preview per home (`/homes/<id>/`) | ✅ |
| 4 | Book a viewing (in person or video, date and time in IST), ask a question | ✅ |
| 5 | Notify me / register interest; requirement alerts | ✅ |
| 6 | Search and share previews (SEO title, description, image per home and locality) | ✅ |
| 7 | Responsive and accessibility refinement (WCAG 2.2 AA) | ✅ (PR #8); Lighthouse/axe still to run |
| 8 | Enquiries delivered to the owner (Netlify Forms and email notification; WhatsApp/email fallback buttons) | 🟡 needs Netlify setup and `CONTACT` |
| 9 | Real photos, deposits, sizes, bathrooms, #674 details, viewing hours | 🟡 |
| 10 | Contact details on the Contact page, footer and Privacy Policy | 🟡 |
| 11 | 360° tours and short videos per home (viewer already built) | 🟡 media |
| 12 | Own domain (e.g. mativio.in) | 🟡 |
| 13 | Visitor statistics (privacy-friendly analytics, consent-aware) | ⬜ |
| 14 | Responsive images (srcset, WebP/AVIF) and font self-hosting | ⬜ (with real photos) |
| 15 | Go live | 🟡 owner decision |

## Phase 2 — Admin panel (needs login and a database; Supabase suggested)

16. Owner/admin login (role-based).
17. Manage listings, photos, statuses and rents without code; this replaces editing `P`. Regenerate share pages automatically.
18. Enquiry inbox with status: New → Contacted → Viewing booked → Closed; viewing confirmation that the tenant sees as confirmed.
19. Tenant records: unit, lease dates, rent, deposit.

## Phase 3 — Rent and leases

20. Rent tracker: due / paid / overdue per unit.
21. Lease renewal reminders at 60, 30 and 7 days.
22. Downloadable rent receipts (PDF).
23. Optional online rent payment via UPI / Razorpay. The current Terms say there are no payments on the site, so update them first.

## Phase 4 — Tenant portal and maintenance

24. Tenant login: lease, rent history, receipts.
25. Maintenance requests raised on the web (plumbing, electrical, etc.) with urgency and photo upload.
26. SLAs (e.g. urgent 4 h, routine 48 h) with countdown and late alerts to the owner.
27. Request tracking: Open → Assigned → In progress → Resolved, with the tenant notified at each step.
28. Planned building maintenance calendar (tank cleaning, lift, pest control, generator).

## Phase 5 — Monitoring and insights

29. CCTV health per building: camera and recorder online, recording status, storage, alerts. This depends on the NVR/DVR brand and model, still to be supplied.
30. Owner dashboard: occupancy, rent collected vs due, open requests and SLA breaches, upcoming renewals, CCTV alerts.
31. WhatsApp and email notifications for the owner and tenants.

## Principles for future phases

- Keep the approved brand, design system and journeys (`docs/brand-guidelines.md`, `docs/design-system.md`). Admin and tenant screens reuse the same tokens in both themes.
- Personal data handling follows the DPDP Act 2023 and Rules 2025: consent, purpose limitation, retention, grievance response within 90 days, breach notice. Update the Privacy Policy before collecting new data types.
- The move from a static site to an app (auth and database) should be planned deliberately. Keep the public site fast and static where possible.
- Every release is reviewed on a preview and shipped in batches with owner approval.

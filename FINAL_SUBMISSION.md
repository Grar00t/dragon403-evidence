# FINAL BUG BOUNTY REPORT - FLYNAS
=======================================

**Title:** High Severity Subdomain Takeover on Multiple Flynas Assets
**Vulnerability Type:** Subdomain Takeover
**Weakness:** CWE-400: Uncontrolled Resource Consumption (Dangling DNS)
**Severity:** High (P2)
**Target:** 
- gift-voucher.flynas.com
- nasplans.flynas.com
- upgrade.flynas.com

**Description:**
During a focused security assessment, I identified multiple subdomains of flynas.com that are vulnerable to Subdomain Takeover. These subdomains are currently pointing to a third-party service (Caravelo) via CNAME records. However, the destination resources (e.g., gift.xy.caravelo.com) are no longer registered or active on the provider's side, resulting in an NXDOMAIN error.

An attacker can claim these orphaned identifiers on the third-party platform to host malicious content under the trusted flynas.com domain.

**Evidence (PoC):**
Run: `host gift-voucher.flynas.com`
Result: `gift-voucher.flynas.com is an alias for gift.xy.caravelo.com.`
Run: `host gift.xy.caravelo.com`
Result: `Host gift.xy.caravelo.com not found: 3(NXDOMAIN)`

**Impact:**
This allows for highly effective phishing attacks, session cookie theft (if scoped to *.flynas.com), and severe brand reputation damage.

**Recommended Fix:**
Remove the dangling CNAME records from the DNS zone file for the affected subdomains.

=======================================
*Prepared with intent and precision by Sulaiman (Seek The Exploit)*

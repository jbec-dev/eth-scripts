# wlFinder
wlFinder is an offline Linux utility for checking whether a candidate password appears in publicly available wordlists.
The main tool is `wlfinder.py`.

## How it works
wlFinder groups wordlists into thematic categories (for example, common passwords and time-related terms).
During a check, categories are processed sequentially, enabling early detection of weak passwords while keeping runtime low.

## Requirements
- Linux environment
- Python 3.x
- [SecLists](https://github.com/danielmiessler/SecLists) installed manually at `/usr/share/seclists`

## Responsible and lawful use
By using this project, you agree that you are solely responsible for ensuring your use complies with all laws, regulations, contractual obligations, and policies that apply to you.

You must only test passwords, systems, and accounts that you own or are explicitly authorized to assess.
Unauthorized security testing may be illegal and may expose you to civil or criminal liability.

## Legal notice and disclaimer
> **Important:** This section is provided for risk disclosure and project transparency only and is **not legal advice**.

- This software is provided **"as is"** and **"as available"**, without warranties of any kind, express or implied, to the maximum extent permitted by applicable law.
- The authors, contributors, and distributors disclaim all implied warranties, including but not limited to merchantability, fitness for a particular purpose, title, non-infringement, accuracy, and uninterrupted operation.
- To the maximum extent permitted by applicable law, the authors, contributors, and distributors are not liable for any direct, indirect, incidental, special, consequential, exemplary, or punitive damages, or for loss of data, profits, business, goodwill, or opportunity, arising from or related to use of this project.
- You are responsible for determining whether local, national, or international laws (including computer misuse, cybersecurity, privacy, labor, consumer protection, and export/sanctions laws) apply to your use.
- If any provision in this README conflicts with applicable law in your jurisdiction, that provision will be interpreted only to the maximum extent enforceable, and the remaining provisions continue in effect.

## Third-party content
wlFinder may rely on third-party resources such as SecLists.
Third-party datasets, trademarks, and content remain the property of their respective owners and are subject to their own licenses and terms.
You are responsible for reviewing and complying with those terms.

## Privacy and data handling
wlFinder is designed as an offline utility.
You are responsible for how password data is sourced, processed, stored, and deleted in your environment, and for compliance with all applicable data protection and employment/privacy obligations.

## License
See [`LICENSE.txt`](./LICENSE.txt) for the governing GPL notice and [`LICENSE.md`](./LICENSE.md) for expanded licensing/legal context.
If there is any inconsistency between these summaries and the GPL license terms, the GPL controls.

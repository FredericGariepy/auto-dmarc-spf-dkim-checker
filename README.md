# Check DMARC, SPF, DKIM for a domain

## Setup
```bash
git clone https://github.com/FredericGariepy/auto-dmarc-spf-dkim-checker.git
cd auto-dmarc-spf-dkim-checker
pip install -r requirements.txt
```
### Add DKIM Selectors if needed
List of DKIM selectors contains top 42 selectors. \
Edit `custom_dkim_selectors_list.py` to further customize DKIM selectors.

## Run

```bash
python main.py
Enter domain: 123cyber.ca
```

def has_asin(url):
    return "dp/" in url or "gp/product" in url

def simplify_affiliate_link(link, affiliate_id):
    parts = link.split("?")
    base_url = parts[0]

    # Remove everything starting from "ref="
    base_url = base_url.split("ref=")[0]

    new_link = base_url + f'?tag={affiliate_id}'
    return new_link

# Input the Amazon link
link = input("Enter the Amazon link (shortened or full): ")
affiliate_id = "aloys03-21"

# Check if link is shortened and expand if necessary
if link.startswith('https://amzn.to/') or link.startswith('http://amzn.to/'):
    full_url = expand_shortened_url(link)
else:
    full_url = link

# Check if link contains ASIN
if has_asin(full_url):
    # Generate simplified affiliate link
    new_link = simplify_affiliate_link(full_url, affiliate_id)
else:
    # If no ASIN, append affiliate tag directly
    new_link = full_url + f'&tag={affiliate_id}'

print(f"The affiliate link is: {new_link}")

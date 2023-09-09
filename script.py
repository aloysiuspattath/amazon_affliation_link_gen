def change_affiliate_id(link, new_affiliate_id):
    parts = link.split("&tag=")
    if len(parts) == 2:
        new_link = parts[0] + "&tag=" + new_affiliate_id
        return new_link
    elif len(parts) == 1:
        new_link = parts[0] + "&tag=" + new_affiliate_id
        return new_link
    else:
        return "Invalid Amazon link"

# Input the Amazon link
old_link = input("Enter the Amazon link: ")
new_affiliate_id = "aloys03-21"

new_link = change_affiliate_id(old_link, new_affiliate_id)
print(new_link)

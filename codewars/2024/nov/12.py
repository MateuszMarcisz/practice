cw = '''Complete the function/method so that it returns the url with anything after the anchor (#) removed.
Examples

"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"

'''

def remove_url_anchor(url):
    return url.split("#")[0]

# print(remove_url_anchor('www.codewars.com#about'))
# print(remove_url_anchor('www.codewars.com?page=1'))

'''Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

'''

def domain_name(url):
    if '//' in url:
        return url.split("//")[1].removeprefix('www.').split('.')[0]
    else:
        return url.removeprefix('www.').split('.')[0]

print(domain_name('http://github.com/carbonfive/raygun'))
print(domain_name('http://www.zombie-bites.com'))
print(domain_name('https://www.cnet.com'))
print(domain_name('icann.org'))
print(domain_name('www.xakep.ru'))
print(domain_name('wreck'))
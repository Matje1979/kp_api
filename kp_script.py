import requests
from pprint import pprint
from PIL import Image
import mimetypes
import os
import gzip
import string
import random
import json

from requests_toolbelt.multipart.encoder import MultipartEncoder


def login():
    session = requests.session()

    # KP
    data = {
        "email": "ibnruzd@yahoo.com",
        "password": "Samopajtonblok61",
        "remember": "yes",
    }
    kp_login_url = "https://www.kupujemprodajem.com/api/web/v1/auth/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 Chrome/51.0.2704.103 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "origin": "https://novi.kupujemprodajem.com",
        "pragma": "no-cache",
        "sec-ch-ua": "'Chromium';v='106', 'Google Chrome';v='106', 'Not;A=Brand';v='99'",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "'macOS'",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-kp-channel": "desktop_react",
        "x-kp-signature": "c83d292dba8529399185f7f9e743040faa478d4f",
        # "authorization": "681ddfe6f0224001053aaa6e7c6d3ebb15c20ef7b97be9910a401c817d62aade",
    }
    response = session.get(kp_login_url, headers=headers, json=data)
    pprint(response.json())
    token = response.json()["token"]
    return token


# def format_prepped_request(prepped, encoding=None):
#     # prepped has .method, .path_url, .headers and .body attribute to view the request
#     encoding = encoding or requests.utils.get_encoding_from_headers(prepped.headers)
#     body = prepped.body.decode(encoding) if encoding else "<binary data>"
#     headers = "\n".join(["{}: {}".format(*hv) for hv in prepped.headers.items()])
#     return f"""\
# {prepped.method} {prepped.path_url} HTTP/1.1
# {headers}

# {body}"""


def upload_photo():
    url = "https://www.kupujemprodajem.com/api/web/v1/file"
    headers = {
        "method": "OPTIONS",
        "authority": "www.kupujemprodajem.com",
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "access-control-request-headers": "x-kp-channel,x-kp-signature",
        "access-control-request-method": "POST",
        "cache-control": "no-cache",
        "origin": "https://novi.kupujemprodajem.com",
        "pragma": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }

    #   --compressed
    session = requests.session()

    filepath = "/Users/damir/projects/kp_api/test_image.jpeg"
    token = login()
    r = session.options(url, headers=headers)
    print(token)
    print(r)
    upload_url = "https://www.kupujemprodajem.com/api/web/v1/file"
    headers = {
        "authority": "www.kupujemprodajem.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "authorization": token,
        "cache-control": "no-cache",
        # "Content-type": "multipart/form-data; boundary=----WebKitFormBoundaryMfy2UdS8DHPuGTqo",
        # "path": "/api/web/v1/file",
        # "cookie": "_fbp=fb.1.1660645341646.710016480; FCNEC=[['AKsRol92dtBEm5RKWj_RAxaL0G9hoWf9DrTCHRh2LdmhAew9SbkGzjQ69fy8RDDVjij2jhJbVT-LQQby4RMkHk24Ei8Cb3u9J-iRiOr7pQB775_qYa_DM8-QekdI3m0xPQipL9Nn4TgbdRHNMo9F3tlO4Ep87o0quw=='],null,[]]; machine_id=22c0f7d631abda548fec5865c98fe77f; NOVI_KUPUJEMPRODAJEM=1; __gads=ID=21ce687314de90bb-229065130cce0079:T=1660645342:S=ALNI_MaEkjgsXUGDNHeA_CbGS3PSseimlg; cookie_consent_v2=1; _gid=GA1.2.935467616.1665951054; __gpi=UID=00000accc260c4f6:T=1660645342:RT=1666027136:S=ALNI_Mb09EYQGfdhc5xQXhQKWMRrEZYzCA; _ga=GA1.2.1342404883.1660645341; KUPUJEMPRODAJEM=e4d3arge4lo7d33fatfmnaqe45; cookie[emailSSL]=damircicic%40gmail.com; cookie[user_idSSL]=c58e89b84c9e83002bbd59e8a3caa487; cookie[password_hashSSL]=d59f1b2a3519d0bc83ca235b418f5c17; _ga_Z0597WW2Y0=GS1.1.1666035479.13.1.1666036536.51.0.0; _ga_MD1JVXY53Y=GS1.1.1666035478.13.1.1666036536.51.0.0; _ga_7X8ZZ1ELGV=GS1.1.1666035479.13.1.1666036536.0.0.0'",
        "origin": "https://novi.kupujemprodajem.com",
        # "pragma": "no-cache",
        "sec-ch-ua": "'Chromium';v='106', 'Google Chrome';v='106', 'Not;A=Brand';v='99'",
        # "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "'macOS'",
        # "sec-fetch-dest": "empty",
        # "sec-fetch-mode": "cors",
        # "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-kp-channel": "desktop_react",
        "x-kp-signature": "2d3aa516351be0ddb877ada248255aeb3a9f1728",
    }

    basewidth = 600

    img = Image.open(filepath)
    width, height = img.size
    print(width, height)
    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(filepath)
    img = Image.open(filepath)
    width, height = img.size
    print(width, height)

    # img = Image.open("/Users/damir/projects/kp_api/test_image.jpeg")
    # img.show()
    mp_encoder = MultipartEncoder(
        fields={
            "use": "ad",
            # plain file object, no filename or mime type produces a
            # Content-Disposition header with just the part name
            "file": (filepath, open(filepath, "rb"), "image/jpeg"),
        }
    )
    headers["Content-Type"] = mp_encoder.content_type
    # print(headers)
    request = requests.Request("POST", upload_url, headers=headers, data=mp_encoder)

    prepped = session.prepare_request(request)
    # print(prepped)
    # print(format_prepped_request(prepped, "utf8"))
    # print()
    r = session.send(prepped, verify=True)

    # with open(filepath, "rb") as fobj:
    # data = fobj.read()
    # files = {"file1": ("test_image.jpeg", data, "image/jpeg")}
    # response = session.post(upload_url, headers=headers, files=files)

    # prepped = session.prepare_request(request)
    # file = "test_image.jpeg"
    # content_type, encoding = mimetypes.guess_type(file)
    # if content_type is None:
    #     content_type = "multipart/form-data"

    # # files = {"file": (file, fobj, content_type)}
    # files = [
    #     ("data", (os.path.basename(filepath), fobj, "video/mp4", {"use": "ad"})),
    # ]

    # response = session.post(upload_url, headers=headers, data=files)

    # print(prepped)
    # print(format_prepped_request(prepped, "utf8"))
    # print()
    # r = session.send(prepped, verify=True)
    # response = session.post(
    #     upload_url,
    #     files=files,
    #     headers=headers,
    #     data={
    #         "Content-Disposition": "form-data",
    #         "name": "file",
    #         "filename": "309250337_1299771354175937_2064720734676653977_n.jpeg",
    #         "Content-Type": "image/jpeg",
    #     },
    # )
    pprint(r.json())

    return r.json()


def id_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def check():
    print("Running check...")
    session = requests.session()
    photo_id = id_generator()

    r = upload_photo()
    token = login()
    print("R: ", r)
    print("Token: ", token)

    r["results"]["id"] = photo_id

    url = "https://www.kupujemprodajem.com/api/web/v1/eds/check"

    headers = {
        "authority": "www.kupujemprodajem.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "authorization": token,
        "cache-control": "no-cache",
        "content-type": "application/json",
        # "cookie": '_fbp=fb.1.1660645341646.710016480; FCNEC=[["AKsRol92dtBEm5RKWj_RAxaL0G9hoWf9DrTCHRh2LdmhAew9SbkGzjQ69fy8RDDVjij2jhJbVT-LQQby4RMkHk24Ei8Cb3u9J-iRiOr7pQB775_qYa_DM8-QekdI3m0xPQipL9Nn4TgbdRHNMo9F3tlO4Ep87o0quw=="],null,[]]; machine_id=22c0f7d631abda548fec5865c98fe77f; NOVI_KUPUJEMPRODAJEM=1; __gads=ID=21ce687314de90bb-229065130cce0079:T=1660645342:S=ALNI_MaEkjgsXUGDNHeA_CbGS3PSseimlg; cookie_consent_v2=1; nps=16026112; zoomInfo=1; _gid=GA1.2.1661791210.1666339618; __gpi=UID=00000accc260c4f6:T=1660645342:RT=1666339618:S=ALNI_Mb09EYQGfdhc5xQXhQKWMRrEZYzCA; _ga=GA1.2.1342404883.1660645341; KUPUJEMPRODAJEM=6vv8tav7ad0f7eqm2f5r3dc2gi; cookie[emailSSL]=ibnruzd%40yahoo.com; cookie[user_idSSL]=b183a98742e0bbc2c2a84df87b8a952d; cookie[password_hashSSL]=bf621030bbe2e2f9161548c356e84332; _ga_7X8ZZ1ELGV=GS1.1.1666339617.20.1.1666340558.0.0.0; _ga_Z0597WW2Y0=GS1.1.1666339617.20.1.1666340558.50.0.0; _ga_MD1JVXY53Y=GS1.1.1666339617.20.1.1666340558.50.0.0',
        "origin": "https://novi.kupujemprodajem.com",
        "pragma": "no-cache",
        "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-kp-channel": "desktop_react",
        "x-kp-signature": "2d3aa516351be0ddb877ada248255aeb3a9f1728",
    }

    data = {
        "data": {
            "kind": "goods",
            "groupSuggestText": "Istorija svega 5",
            "categoryId": 8,
            "groupId": 305,
            "name": "Istorija svega 5",
            "type": "sell",
            "price": "20000",
            "currency": "rsd",
            "priceText": "",
            "priceFixed": "yes",
            "description": "<p>Novo</p>",
            "condition": "as-new",
            "exchange": "",
            "locationId": 110,
            "owner": "Damir Cicic",
            "phone": "",
            "photos": [r["results"]],
            "kpizlog": "",
            "g-recaptcha-response": "",
            "adId": "",
            "adClass": "",
        },
        "checkFields": {
            "kind": True,
            "groupSuggestText": True,
            "categoryId": True,
            "groupId": True,
            "adId": True,
            "adClass": True,
            "name": True,
            "type": True,
            "price": True,
            "currency": True,
            "priceText": True,
            "priceFixed": True,
            "description": True,
            "condition": True,
            "exchange": True,
            "locationId": True,
            "owner": True,
            "phone": True,
            "photos": True,
            "kpizlog": True,
            "g-recaptcha-response": True,
        },
    }

    request = requests.Request("POST", url, headers=headers, data=data)
    prepped = session.prepare_request(request)
    r = session.send(prepped, verify=False)

    return r.json()


def post_add():
    # import pdb

    r = upload_photo()
    # r = json.loads(r)
    # pdb.set_trace()
    photo = r["results"]
    # pdb.set_trace()
    url = "https://www.kupujemprodajem.com/api/web/v1/eds/save"
    session = requests.session()

    data = {
        "data": {
            "kind": "goods",
            "groupSuggestText": "Istorija kolaca",
            "categoryId": 8,
            "groupId": 305,
            "name": "Istorija kolaca",
            "type": "sell",
            "price": "1500",
            "currency": "rsd",
            "priceText": "",
            "priceFixed": "yes",
            "description": "<p>Super knjiga!</p>",
            "condition": "as-new",
            "exchange": "",
            "locationId": 1,
            "owner": "Damir Cicic",
            "phone": "",
            "photos": [photo],
            "kpizlog": "",
            "g-recaptcha-response": "",
            "promoType": "none",
            "promoAdcreate": "",
            "highlighted": "",
            "promoLink": "",
            "website": "",
            "promoVideo": "",
            "videoUrl": "",
            "promoGoldAd": "",
            "declarationType": "person",
            "accept": "yes",
            "agreements": "",
            "agreement": "",
            "dCompanyName": "",
            "dAddress": "",
            "dRegistrationNumber": "",
            "swear": "",
            "regNumberRealEstateAgentId": "",
            "regNumberHid": "",
            "regNumberHealthcareLicenseId": "",
            "regNumberApartmentsCategorizationId": "",
            "regNumberPetOwnerIdValue": "",
            "adId": "",
            "adClass": "",
        },
    }
    headers = {
        "authority": "www.kupujemprodajem.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "content-type": "application/json",
        # "cookie": "_fbp=fb.1.1660645341646.710016480; FCNEC=[['AKsRol92dtBEm5RKWj_RAxaL0G9hoWf9DrTCHRh2LdmhAew9SbkGzjQ69fy8RDDVjij2jhJbVT-LQQby4RMkHk24Ei8Cb3u9J-iRiOr7pQB775_qYa_DM8-QekdI3m0xPQipL9Nn4TgbdRHNMo9F3tlO4Ep87o0quw=='],null,[]]; machine_id=22c0f7d631abda548fec5865c98fe77f; NOVI_KUPUJEMPRODAJEM=1; __gads=ID=21ce687314de90bb-229065130cce0079:T=1660645342:S=ALNI_MaEkjgsXUGDNHeA_CbGS3PSseimlg; cookie_consent_v2=1; _gid=GA1.2.935467616.1665951054; cookie[user_idSSL]=c58e89b84c9e83002bbd59e8a3caa487; KUPUJEMPRODAJEM=s3uv37qbjkhl99uoegoo216a9r; cookie[emailSSL]=damircicic%40gmail.com; cookie[password_hashSSL]=d59f1b2a3519d0bc83ca235b418f5c17; __gpi=UID=00000accc260c4f6:T=1660645342:RT=1666087574:S=ALNI_Mb09EYQGfdhc5xQXhQKWMRrEZYzCA; _ga=GA1.2.1342404883.1660645341; _gat_gtag_UA_3494319_1=1; _ga_MD1JVXY53Y=GS1.1.1666091192.15.0.1666091192.60.0.0; _ga_7X8ZZ1ELGV=GS1.1.1666091192.15.0.1666091192.0.0.0; _ga_Z0597WW2Y0=GS1.1.1666091192.15.0.1666091192.60.0.0",
        "origin": "https://novi.kupujemprodajem.com",
        "pragma": "no-cache",
        "sec-ch-ua": "'Chromium';v='106', 'Google Chrome';v='106', 'Not;A=Brand';v='99'",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "'macOS'",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "x-kp-channel": "desktop_react",
        "x-kp-signature": "efec95457f496b26ae55f415cf7918230cbe2aa0",
    }

    response = session.get(url, headers=headers, data=data)
    pprint(response.json())
    return response

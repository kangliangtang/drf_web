
import hashlib
import base64


def md5_encry(s):
    """md5加密"""
    obj = hashlib.md5()
    # 声明encode
    obj.update(s.encode(encoding='utf-8'))
    encry_ret = obj.hexdigest()
    return encry_ret


def base64_encry(s):
    """base64加密"""
    base64_encry = base64.b64encode(s.encode('utf-8'))
    return base64_encry


def base64_decry(s):
    """base64解密"""
    base64_decry = (base64.b64decode(base64_encry)).decode('utf-8')
    return base64_decry



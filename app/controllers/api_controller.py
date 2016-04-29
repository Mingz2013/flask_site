__author__ = 'zhaojm'


from qiniu import Auth



def get_token(access_key, secret_key):
    q = Auth(access_key, secret_key)

    # 上传策略仅指定空间名和上传后的文件名，其他参数仅为默认值
    token = q.upload_token("activity", "activity.jpg")

    # 上传策略除空间名和上传后的文件名外，指定上传凭证有效期为7200s
    # callcakurl为"http://callback.do"，
    # callbackBody为原始文件名和文件Etag值
    # token2 = q.upload_token(bucket_name, key, 7200, {'callbackUrl':"http://callback.do", 'callbackBody':"name=$(fname)&hash=$(etag)"})

    return token

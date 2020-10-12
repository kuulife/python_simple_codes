from speedtest import Speedtest

st = Speedtest()

downl = st.download()
upl = st.upload()
ping = st.results.ping
st.get_servers([])
print(f'Download: {downl}')
print(f'Upload: {upl}')
print(f'ping: {ping}')
 
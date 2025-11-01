import streamlit as st

gelir = st.number_input("Gelirinizi Giriniz: ")
ucret_gelir = st.selectbox("Geliriniz ücret geliri mi ?",("Evet","Hayır"))
st.title("Vergi Hesaplama...")

if gelir < 158000:
  vergi = gelir * 15 / 100
  net_kazanc = gelir - vergi
  st.write("1.Vergi Dilimindesiniz.")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

elif 158000 < gelir < 330000:
  vergi = (gelir-23700) * 20 / 100
  net_kazanc = gelir - vergi
  st.write("2.Vergi Dilimindesiniz.")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

elif 330000 < gelir < 800000 and ucret_gelir == "Hayır":
  vergi = (gelir-58100) * 27 / 100
  net_kazanc = gelir - vergi
  st.write("3.Vergi Dilimindesiniz.")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

elif 330000 < gelir < 1200000 and ucret_gelir == "Evet":
  vergi = (gelir-58100) * 27 / 100
  net_kazanc = gelir - vergi
  st.write("3.Vergi Dilimindesiniz (Ücret Geliri).")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

elif 800000 < gelir < 4300000 and ucret_gelir == "Hayır":
  vergi = (gelir-185000) * 35 / 100
  net_kazanc = gelir - vergi
  st.write("4.Vergi Dilimindesiniz.")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

elif 1200000 < gelir < 4300000 and ucret_gelir == "Evet":
  vergi = (gelir-293000) * 35 / 100
  net_kazanc = gelir - vergi
  st.write("4.Vergi Dilimindesiniz.(Ücret Geliri)")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

elif 4300000 < gelir and ucret_gelir == "Hayır":
  vergi = (gelir-1410000) * 40 / 100
  net_kazanc = gelir - vergi
  st.write("5.Vergi Dilimindesiniz.")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

elif 4300000 < gelir and ucret_gelir == "Evet":
  vergi = (gelir-1378000) * 40 / 100
  net_kazanc = gelir - vergi
  st.write("5.Vergi Dilimindesiniz. (Ücret Geliri)")
  st.write("Net kazancınız: ",net_kazanc)
  st.write("Ödeyeceğiniz vergi Miktarı: ",vergi)

else:
    st.write("Hata")

# streamlit run "dosya adı" yazılarak çalıştırılır
# pip freeze > requirements.txt  ile text dosyası haline getirilir, gerekli kütüphaneleri hazırlar.
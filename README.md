# Classical Cryptography Algorithms - Caesar Cipher, Vigenère Cipher, XOR Cipher

## Mục tiêu

Đây là một dự án thực hành để tìm hiểu và triển khai ba thuật toán mã hóa cổ điển: **Caesar Cipher**, **Vigenère Cipher**, và **XOR Cipher**. Dự án giúp bạn hiểu về các thuật toán mã hóa cơ bản và cách triển khai chúng bằng Python.

## Cấu trúc dự án


## Các thuật toán mã hóa

### 1. **Caesar Cipher (caesar_cipher.py)**

#### Mô tả:
**Caesar Cipher** là một thuật toán mã hóa đơn giản trong đó mỗi ký tự trong văn bản được dịch chuyển theo một số lượng cố định. Ví dụ, với một dịch chuyển 3, ký tự 'A' sẽ trở thành 'D', 'B' sẽ thành 'E', và v.v.

#### Cách hoạt động:
- Chuyển mỗi ký tự trong chuỗi văn bản vào bảng chữ cái, dịch chuyển theo một giá trị (shift) đã cho.
- Nếu ký tự là chữ cái (in hoa hoặc thường), ta áp dụng dịch chuyển; nếu không phải chữ cái (như dấu cách, dấu chấm), giữ nguyên.
  
#### Hàm mã hóa:

```python
def caesar_encrypt(plaintext, shift):
    result = ''
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Giữ nguyên các ký tự không phải chữ cái
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)


Ví dụ sử dụng :
plaintext = "Hello, World!"
shift = 3
encrypted = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Original:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)


Mô tả:

Vigenère Cipher là một phương pháp mã hóa thay đổi khóa, trong đó mỗi chữ cái trong văn bản gốc sẽ được dịch chuyển theo giá trị tương ứng với chữ cái của từ khóa.

Cách hoạt động:

Sử dụng một từ khóa để xác định độ dịch chuyển cho mỗi chữ cái. Chữ cái trong văn bản gốc được mã hóa bằng cách cộng giá trị của nó với giá trị của chữ cái tương ứng trong từ khóa.

Nếu văn bản dài hơn từ khóa, từ khóa sẽ được lặp lại để đủ độ dài.

Hàm mã hóa:
def vigenere_encrypt(plaintext, key):
    result = ''
    key_index = 0
    key = key.lower()
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char.lower()) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char  # Giữ nguyên các ký tự không phải chữ cái
    return result

Hàm giải mã: 
def vigenere_decrypt(ciphertext, key):
    result = ''
    key_index = 0
    key = key.lower()
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char.lower()) - shift_base - shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char  # Giữ nguyên các ký tự không phải chữ cái
    return result

Ví dụ sử dụng:
plaintext = "Hello, World!"
key = "KEY"
encrypted = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Original:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)



Mô tả:

XOR Cipher là một phương pháp mã hóa đơn giản sử dụng toán tử XOR bitwise. Mỗi ký tự trong văn bản được mã hóa hoặc giải mã bằng cách áp dụng phép toán XOR với một khóa số nguyên.

Cách hoạt động:

Mỗi ký tự trong văn bản được chuyển thành mã ASCII, sau đó thực hiện phép toán XOR giữa mã ASCII của ký tự và khóa.

Do tính chất đối xứng của phép toán XOR, việc giải mã lại là quá trình giống như mã hóa.

Hàm giải mã:
def xor_encrypt_decrypt(text, key):
    result = ''.join(chr(ord(char) ^ key) for char in text)
    return result

Ví dụ sử dụng:
plaintext = "Hello, World!"
key = 123  # Một giá trị số cho khóa XOR
encrypted = xor_encrypt_decrypt(plaintext, key)
decrypted = xor_encrypt_decrypt(encrypted, key)

print("Original:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)



Caesar Cipher: Dịch chuyển mỗi ký tự trong văn bản theo một giá trị cố định.

Vigenère Cipher: Sử dụng từ khóa để thay đổi độ dịch chuyển cho mỗi ký tự trong văn bản.

XOR Cipher: Sử dụng phép toán XOR để mã hóa và giải mã văn bản với một khóa.




Demo tấn công, phân tích độ mạnh/yếu và ứng dụng giáo dục
Mục tiêu

Thực hành các tấn công cơ bản vào Caesar, Vigenère, XOR để hiểu điểm mạnh/yếu.

Viết script demo tự động: brute-force, tấn công dựa trên phân tích tần suất, Kasiski/Friedman cho Vigenère, tấn công XOR khi khóa bị tái sử dụng (key reuse / crib-dragging).

Ghi nhận kết quả và rút ra kết luận về ứng dụng giáo dục.

Cấu trúc demo đề xuất

Thêm file mới vào project:

crypto_project/
├── attacks/
│   ├── caesar_attack.py
│   ├── vigenere_attack.py
│   └── xor_attack.py


Mỗi file chứa code demo + ví dụ chạy.

1) Caesar — Demo brute-force

Ý tưởng: chỉ có 26 khả năng. Brute-force sẽ lặp shift từ 0..25 và in ra khả năng giải mã; chọn kết quả hợp lý.

attacks/caesar_attack.py:

from caesar_cipher import caesar_decrypt

def brute_force_caesar(ciphertext):
    candidates = []
    for shift in range(26):
        plain = caesar_decrypt(ciphertext, shift)
        candidates.append((shift, plain))
    return candidates

if __name__ == "__main__":
    c = "Khoor, Zruog!"  # ví dụ: "Hello, World!" shift=3
    for shift, txt in brute_force_caesar(c):
        print(f"shift={shift:2d}: {txt}")


Chạy: python attacks/caesar_attack.py
Kết luận giáo dục: Caesar yếu vì không gian khóa nhỏ; thích hợp để dạy về brute-force và khái niệm entropy/space key.

2) Vigenère — Demo Kasiski / Friedman + chi-squared shift để tìm khóa

Ý tưởng demo:

Dùng Kasiski để đo lặp chuỗi và ước lượng độ dài khóa.

Dùng Friedman Index of Coincidence (IC) để ước lượng độ dài khóa.

Tách ciphertext theo vị trí trong khóa, dùng phân tích tần suất / chi-squared để xác định shift cho từng cột => phục hồi khóa.

attacks/vigenere_attack.py (một bản đơn giản, không tối ưu nhưng có thể chạy):

import re
from collections import Counter
from math import fabs
from vigenere_cipher import vigenere_decrypt

alphabet = "abcdefghijklmnopqrstuvwxyz"

def friedman_ic(text):
    # chỉ tính cho letters
    s = ''.join([c for c in text.lower() if c.isalpha()])
    N = len(s)
    freqs = Counter(s)
    ic = sum(v*(v-1) for v in freqs.values()) / (N*(N-1)) if N > 1 else 0
    return ic

def kasiski_examination(text, min_len=3):
    text = re.sub('[^A-Za-z]', '', text).lower()
    distances = []
    for seq_len in range(min_len, 6):
        seq_pos = {}
        for i in range(len(text)-seq_len):
            seq = text[i:i+seq_len]
            if seq in seq_pos:
                seq_pos[seq].append(i)
            else:
                seq_pos[seq] = [i]
        for seq, pos_list in seq_pos.items():
            if len(pos_list) > 1:
                for i in range(len(pos_list)-1):
                    distances.append(pos_list[i+1] - pos_list[i])
    return distances

def likely_key_lengths_from_kasiski(distances):
    # trả về các ước số phổ biến
    from math import gcd
    from collections import Counter
    if not distances: return []
    g = distances[0]
    for d in distances[1:]:
        g = gcd(g, d)
    # cũng tính ước số chung phổ biến
    factors = []
    for d in distances:
        for k in range(2, 21):
            if d % k == 0:
                factors.append(k)
    return Counter(factors).most_common(5)

def chi_squared_score(seq):
    # seq là chuỗi các chữ cái (lower)
    expected_freq = {
        'a':8.167,'b':1.492,'c':2.782,'d':4.253,'e':12.702,'f':2.228,'g':2.015,
        'h':6.094,'i':6.966,'j':0.153,'k':0.772,'l':4.025,'m':2.406,'n':6.749,
        'o':7.507,'p':1.929,'q':0.095,'r':5.987,'s':6.327,'t':9.056,'u':2.758,
        'v':0.978,'w':2.360,'x':0.150,'y':1.974,'z':0.074
    }
    N = len(seq)
    if N == 0: return float('inf')
    score = 0.0
    freq = Counter(seq)
    for ch in alphabet:
        O = freq.get(ch, 0)
        E = expected_freq[ch] * N / 100.0
        score += (O - E) ** 2 / E if E>0 else 0
    return score

def break_vigenere(ciphertext, max_key_len=12):
    text = ''.join([c for c in ciphertext if c.isalpha()])
    # try key lengths 1..max_key_len
    best = None
    for k in range(1, max_key_len+1):
        key = ''
        total_score = 0
        for i in range(k):
            seq = ''.join(text[j] for j in range(i, len(text), k)).lower()
            # try all shifts for this column
            best_shift = None
            best_score = float('inf')
            for s in range(26):
                # shift back by s
                shifted = ''.join(chr((ord(ch)-97 - s) % 26 + 97) for ch in seq)
                sc = chi_squared_score(shifted)
                if sc < best_score:
                    best_score = sc
                    best_shift = s
            key += chr(best_shift + 97)
            total_score += best_score
        if best is None or total_score < best[0]:
            best = (total_score, k, key)
    if best:
        _, k, key = best
        plaintext = vigenere_decrypt(ciphertext, key)
        return {'key': key, 'key_len': k, 'plaintext': plaintext}
    return None

if __name__ == "__main__":
    c = "Lxfopvefrnhr"  # "attackatdawn" with key "lemon" => just sample
    print("Friedman IC:", friedman_ic(c))
    print("Kasiski distances:", kasiski_examination(c))
    res = break_vigenere(c, max_key_len=8)
    print(res)


Chạy: python attacks/vigenere_attack.py
Kết luận giáo dục:

Vigenère mạnh hơn Caesar vì khóa chuỗi, nhưng nếu khóa ngắn hoặc lặp lại, tấn công tần suất + Kasiski/Friedman có thể phục hồi khóa.

Dùng để dạy khái niệm phân tích tần suất, IC, ước lượng độ dài khóa, và tại sao khóa không lặp lại (one-time pad) mới là an toàn hoàn hảo.

3) XOR — Demo tấn công khi khóa ngắn hoặc tái sử dụng (key reuse)

Scenarios to demo:

Khi key là 1 byte: brute-force thử 0..255.

Khi key ngắn (n byte) nhưng dùng để mã hóa nhiều plaintexts (key reuse) → attacker có thể XOR hai ciphertexts để loại bỏ key: c1 ^ c2 = p1 ^ p2 → dùng crib-dragging để tìm từ khóa/tiếp cận plaintext.

Khi key là one-time pad (ngẫu nhiên, không tái sử dụng) và bí mật, an toàn; nhưng thực tế thường reuse -> insecure.

attacks/xor_attack.py:

from xor_cipher import xor_encrypt_decrypt

# brute force when key is single byte
def brute_force_xor_single_byte(ciphertext):
    candidates = []
    for k in range(256):
        try:
            plain = ''.join(chr(ord(c) ^ k) for c in ciphertext)
            # crude filter: require many printable chars
            if sum(1 for ch in plain if 32 <= ord(ch) < 127) / max(1, len(plain)) > 0.9:
                candidates.append((k, plain))
        except Exception:
            continue
    return candidates

# crib-dragging on two ciphertexts with same key
def crib_drag(c1, c2, crib):
    # c1 and c2 are strings (same key used)
    # p1 ^ p2 = c1 ^ c2
    x = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(c1, c2))
    results = []
    for i in range(len(x)-len(crib)+1):
        segment = x[i:i+len(crib)]
        # if segment XOR crib yields printable text, print candidate
        p1_segment = ''.join(chr(ord(segment[j]) ^ ord(crib[j])) for j in range(len(crib)))
        if all(32 <= ord(ch) < 127 for ch in p1_segment):
            results.append((i, p1_segment))
    return results

if __name__ == "__main__":
    pt = "Hello, World!"
    key = 123
    ct = xor_encrypt_decrypt(pt, key)
    print("ciphertext repr:", [ord(c) for c in ct])
    print("brute candidates:", brute_force_xor_single_byte(ct))

    # demo key reuse
    p1 = "Attack at dawn"
    p2 = "Send more money"
    key = "secret"  # short key reused
    c1 = ''.join(chr(ord(a) ^ ord(key[i % len(key)])) for i,a in enumerate(p1))
    c2 = ''.join(chr(ord(a) ^ ord(key[i % len(key)])) for i,a in enumerate(p2))
    print("crib drag for ' the ' on p1/p2:", crib_drag(c1, c2, " the "))


Chạy: python attacks/xor_attack.py
Kết luận giáo dục:

XOR với key 1 byte rất yếu (brute-force).

Reuse key nhiều plaintexts cho phép tấn công mạnh (crib-dragging).

One-time pad nguyên lý an toàn nhưng khó thực hiện đúng (khó tạo key đủ dài & ngẫu nhiên và đảm bảo không reuse).
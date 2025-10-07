#!/usr/bin/env python3
# logger_utils.py
# AES-GCM helper utilities for TypeScope

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64
from typing import Optional

def derive_key_from_password(password: str) -> bytes:
    """
        Lightweight KDF for demo purposes (SHA-256). For production use Argon2/PBKDF2 with salt.
            Returns 32 bytes key.
                """
                    from hashlib import sha256
                        return sha256(password.encode("utf-8")).digest()

                        def encrypt_bytes(key: bytes, plaintext: bytes) -> bytes:
                            """
                                Encrypt plaintext with AES-GCM. Return base64(nonce || ciphertext || tag).
                                    """
                                        aesgcm = AESGCM(key)
                                            nonce = os.urandom(12)
                                                ct = aesgcm.encrypt(nonce, plaintext, None)
                                                    blob = nonce + ct
                                                        return base64.b64encode(blob)

                                                        def decrypt_bytes(key: bytes, b64blob: bytes) -> bytes:
                                                            """
                                                                Decrypt base64(nonce || ciphertext || tag) and return plaintext bytes.
                                                                    """
                                                                        blob = base64.b64decode(b64blob)
                                                                            if len(blob) < 13:
                                                                                    raise ValueError("Invalid ciphertext")
                                                                                        nonce = blob[:12]
                                                                                            ct = blob[12:]
                                                                                                aesgcm = AESGCM(key)
                                                                                                    return aesgcm.decrypt(nonce, ct, None)
                                                                                                    
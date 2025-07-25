/**
 * Created by max.rozdobudko@gmail.com on 03.02.2020.
 */
package com.github.airext.openssl.test.suite.rsa.theory {
import com.github.airext.OpenSSL;
import com.github.airext.openssl.test.data.KeyPair;
import com.github.airext.openssl.test.data.TestData;
import com.github.airext.openssl.test.helper.ByteArrayGenerator;
import com.github.airext.openssl.test.helper.FileUtils;
import com.github.airext.openssl.test.helper.Variants;

import flash.filesystem.File;

import flash.utils.ByteArray;

import org.flexunit.asserts.assertEquals;

[RunWith("org.flexunit.experimental.theories.Theories")]
public class TheoryRSA {

    [DataPoints]
    [ArrayElementType("flash.utils.ByteArray")]
    public static var data: Array = ByteArrayGenerator.generateMany(Variants.generatingDataCount, 32, 245);

    [DataPoints]
    [ArrayElementType("com.github.airext.openssl.test.data.KeyPair")]
    public static var keyPairs: Array = [
        new KeyPair(
            FileUtils.readBytes(File.applicationDirectory.resolvePath("certificates/Server1 - Public key.pem")),
            FileUtils.readBytes(File.applicationDirectory.resolvePath("certificates/Server1 - Private key.pem"))
        )
    ];

    [Theory]
    public function encryptDecrypt(data: ByteArray, keyPair: KeyPair): void {
        var encrypted: ByteArray = OpenSSL.shared.rsaEncrypt(data, keyPair.publicKey);
        var decrypted: ByteArray = OpenSSL.shared.rsaDecrypt(encrypted, keyPair.privateKey);

        assertEquals(data.readUTFBytes(data.length), decrypted.readUTFBytes(decrypted.length));
    }
}
}
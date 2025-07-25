/**
 * Created by max.rozdobudko@gmail.com on 26.01.2020.
 */
package com.github.airext.openssl.test.data {

public class TestData {

    public static const keyPairs1024: Vector.<KeyPair> = new <KeyPair>[
        new KeyPair("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCAoOU2OGebf2yWxVi1u0SIBa73rrgblZz8x7XNSzNrwXW+kDK0KW3DbUIn6VpXFfZhYT4MgFtpkHBfxQC6/gyzoH+hETrJU9Ntx+v3RFakFNbX5MzYxzpNOVbG1MsbS9CYLP96XWuslInSfAe4zq4jzQIAY2T191ZLSiGi/pWcYwIDAQAB", "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAICg5TY4Z5t/bJbFWLW7RIgFrveuuBuVnPzHtc1LM2vBdb6QMrQpbcNtQifpWlcV9mFhPgyAW2mQcF/FALr+DLOgf6EROslT023H6/dEVqQU1tfkzNjHOk05VsbUyxtL0Jgs/3pda6yUidJ8B7jOriPNAgBjZPX3VktKIaL+lZxjAgMBAAECgYAsVUgrE+3Bzn1iycn1eQH5z9uqSnHyL/LXvQ2QIGcssJUghRq0tcK7JKE0mF0mvs8YaSe1r1fSXpIcsA28ZWuC0Guf95+Vm9tVVNc2+OaoSXOxcVvnH0fyPPpaTZDKiM0XJxSTDkW53emJUcJVxYMTPcH+ndhX8aTsRcr8OY624QJBAMFZPqc4t6CfNvnV8A2gZa3IDxLL08UfG9N17tXVT12HTvKFXvrqxtoxRwmKzNFJfNHeirLWN6YJnP75V9j06v8CQQCqTvQruXnK8r0U78TAx7qpSmkzDGSUxYpJfh1nJcI2GWoAuYzSsiDY6FotZzZWyCbEf01A9SHZHBtKZSdq9IKdAkAVj2oZI432b0qmGWEnY9dyxXhI1EnNFWb48ZGsbpjnCQuYp56rxDpgYlZVjhDA1b0BehtlTdXuweur0woku0rpAkEAoYm2C+snXJqVQlCSXRCVOpH76pGsrXgZTNA0b2vfJJVCeGGG8ypGAbeSIVKute2u596flids7ZO9RvlfRBGb+QJBAJ3hgdBcBRAojcYM0U7wrr3dv0543O+kVpbFRKu04yuPRApCUIIhEP1ViGEg6vLTnacFTb1YqcrNsoMl2YQ269w="),
    ];

    public static const keyPairs2048: Vector.<KeyPair> = new <KeyPair>[
        new KeyPair("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"),
    ];

    public static const keyPairs4096: Vector.<KeyPair> = new <KeyPair>[
//        new KeyPair("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"),
        new KeyPair(
            "-----BEGIN PUBLIC KEY-----\n" +
            "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy8Dbv8prpJ/0kKhlGeJY\n" +
            "ozo2t60EG8L0561g13R29LvMR5hyvGZlGJpmn65+A4xHXInJYiPuKzrKUnApeLZ+\n" +
            "vw1HocOAZtWK0z3r26uA8kQYOKX9Qt/DbCdvsF9wF8gRK0ptx9M6R13NvBxvVQAp\n" +
            "fc9jB9nTzphOgM4JiEYvlV8FLhg9yZovMYd6Wwf3aoXK891VQxTr/kQYoq1Yp+68\n" +
            "i6T4nNq7NWC+UNVjQHxNQMQMzU6lWCX8zyg3yH88OAQkUXIXKfQ+NkvYQ1cxaMoV\n" +
            "PpY72+eVthKzpMeyHkBn7ciumk5qgLTEJAfWZpe4f4eFZj/Rc8Y8Jj2IS5kVPjUy\n" +
            "wQIDAQAB\n" +
            "-----END PUBLIC KEY-----\n",
            "-----BEGIN RSA PRIVATE KEY-----\n" +
            "MIIEowIBAAKCAQEAy8Dbv8prpJ/0kKhlGeJYozo2t60EG8L0561g13R29LvMR5hy\n" +
            "vGZlGJpmn65+A4xHXInJYiPuKzrKUnApeLZ+vw1HocOAZtWK0z3r26uA8kQYOKX9\n" +
            "Qt/DbCdvsF9wF8gRK0ptx9M6R13NvBxvVQApfc9jB9nTzphOgM4JiEYvlV8FLhg9\n" +
            "yZovMYd6Wwf3aoXK891VQxTr/kQYoq1Yp+68i6T4nNq7NWC+UNVjQHxNQMQMzU6l\n" +
            "WCX8zyg3yH88OAQkUXIXKfQ+NkvYQ1cxaMoVPpY72+eVthKzpMeyHkBn7ciumk5q\n" +
            "gLTEJAfWZpe4f4eFZj/Rc8Y8Jj2IS5kVPjUywQIDAQABAoIBADhg1u1Mv1hAAlX8\n" +
            "omz1Gn2f4AAW2aos2cM5UDCNw1SYmj+9SRIkaxjRsE/C4o9sw1oxrg1/z6kajV0e\n" +
            "N/t008FdlVKHXAIYWF93JMoVvIpMmT8jft6AN/y3NMpivgt2inmmEJZYNioFJKZG\n" +
            "X+/vKYvsVISZm2fw8NfnKvAQK55yu+GRWBZGOeS9K+LbYvOwcrjKhHz66m4bedKd\n" +
            "gVAix6NE5iwmjNXktSQlJMCjbtdNXg/xo1/G4kG2p/MO1HLcKfe1N5FgBiXj3Qjl\n" +
            "vgvjJZkh1as2KTgaPOBqZaP03738VnYg23ISyvfT/teArVGtxrmFP7939EvJFKpF\n" +
            "1wTxuDkCgYEA7t0DR37zt+dEJy+5vm7zSmN97VenwQJFWMiulkHGa0yU3lLasxxu\n" +
            "m0oUtndIjenIvSx6t3Y+agK2F3EPbb0AZ5wZ1p1IXs4vktgeQwSSBdqcM8LZFDvZ\n" +
            "uPboQnJoRdIkd62XnP5ekIEIBAfOp8v2wFpSfE7nNH2u4CpAXNSF9HsCgYEA2l8D\n" +
            "JrDE5m9Kkn+J4l+AdGfeBL1igPF3DnuPoV67BpgiaAgI4h25UJzXiDKKoa706S0D\n" +
            "4XB74zOLX11MaGPMIdhlG+SgeQfNoC5lE4ZWXNyESJH1SVgRGT9nBC2vtL6bxCVV\n" +
            "WBkTeC5D6c/QXcai6yw6OYyNNdp0uznKURe1xvMCgYBVYYcEjWqMuAvyferFGV+5\n" +
            "nWqr5gM+yJMFM2bEqupD/HHSLoeiMm2O8KIKvwSeRYzNohKTdZ7FwgZYxr8fGMoG\n" +
            "PxQ1VK9DxCvZL4tRpVaU5Rmknud9hg9DQG6xIbgIDR+f79sb8QjYWmcFGc1SyWOA\n" +
            "SkjlykZ2yt4xnqi3BfiD9QKBgGqLgRYXmXp1QoVIBRaWUi55nzHg1XbkWZqPXvz1\n" +
            "I3uMLv1jLjJlHk3euKqTPmC05HoApKwSHeA0/gOBmg404xyAYJTDcCidTg6hlF96\n" +
            "ZBja3xApZuxqM62F6dV4FQqzFX0WWhWp5n301N33r0qR6FumMKJzmVJ1TA8tmzEF\n" +
            "yINRAoGBAJqioYs8rK6eXzA8ywYLjqTLu/yQSLBn/4ta36K8DyCoLNlNxSuox+A5\n" +
            "w6z2vEfRVQDq4Hm4vBzjdi3QfYLNkTiTqLcvgWZ+eX44ogXtdTDO7c+GeMKWz4XX\n" +
            "uJSUVL5+CVjKLjZEJ6Qc2WZLl94xSwL71E41H4YciVnSCQxVc4Jw\n" +
            "-----END RSA PRIVATE KEY-----\n"
        )
    ];

    public static const phrases: Array = [
        "The quick brown fox jumps over the lazy dog"
    ];
}
}
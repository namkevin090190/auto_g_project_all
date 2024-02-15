import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

public class CryptoUtil {
  private static Charset CHARSET = StandardCharsets.UTF_8;

  public static String generateEncryptedSecret(String baseSecret, String transactionId) {
    String secret = baseSecret;

    // K = base32(secret_key + transactionId)
    
    secret = secret + transactionId;
    secret = Base32String.encode(secret.getBytes(CHARSET));

    return secret;
  }
}

import java.lang.reflect.UndeclaredThrowableException;
import java.security.GeneralSecurityException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.math.BigInteger;
import java.util.TimeZone;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
//
import java.util.HashMap;
import java.util.Locale;

//
public class Main {
  public static void main(String[] args) {
    // Dump device-id = PERFORMANCE-DEVICE-TESTING
    String secret = "PLTIUKHIOPBZWIKZKNYL6EBKPY======";
    String transactionId = args[0];
    int digits = 6;
    long period = 30;

    String encryptedSecret = CryptoUtil.generateEncryptedSecret(
        secret,
        transactionId);
    long currentSecond = TotpUtil.getCurrentTimeSecond();

    String code = TotpUtil.generateOTP(
        encryptedSecret,
        currentSecond,
        period,
        digits);

    System.out.println(code);
  }
}
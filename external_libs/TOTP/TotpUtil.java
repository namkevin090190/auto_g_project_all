import java.security.GeneralSecurityException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class TotpUtil {
    private final static int REFLECTIVE_PIN_LENGTH = 9;
    private static int digits;

    public static long getCurrentTimeSecond() {
      try {
        return System.currentTimeMillis() / 1000;
      } catch (IllegalStateException e) {
        return System.currentTimeMillis() / 1000;
      }
    }

    public static long getRemainingSecond(long time, long period) {
        long nextCounter = getCounterAtTime(time, period) + 1;
        return Math.max(0, Math.min(nextCounter * period - time, period));
    }

    public static String generateOTP(String secret, long time, long period, int digit) {
        long counter = getCounterAtTime(time, period);
        digits = digit;

        try {
            return computePin(secret, counter,null);
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
    }

    private static long getCounterAtTime(long time, long period) {
        long timeSinceStartTime = time;

        if (timeSinceStartTime >= 0) {
            return timeSinceStartTime / period;
        } else {
            return (timeSinceStartTime - (period - 1)) / period;
        }
    }

    private static String computePin(String secret, long counter, byte[] challenge)
            throws Exception {
        try {
            PasscodeGenerator.Signer signer = getSigningOracle(secret);
            PasscodeGenerator pcg = new PasscodeGenerator(signer,
                    (challenge == null) ? digits : REFLECTIVE_PIN_LENGTH);

            return (challenge == null) ? pcg.generateResponseCode(counter)
                    : pcg.generateResponseCode(counter, challenge);
        } catch (GeneralSecurityException e) {
            throw new Exception("Crypto failure", e);
        }
    }

    private static PasscodeGenerator.Signer getSigningOracle(String secret) {
        try {
            byte[] keyBytes = decodeKey(secret);
            final Mac mac = Mac.getInstance("HmacSHA512");
            mac.init(new SecretKeySpec(keyBytes, ""));
            //
            return new PasscodeGenerator.Signer() {
                @Override
                public byte[] sign(byte[] data) {
                    return mac.doFinal(data);
                }
            };
        } catch (Exception error) {
            
        }

        return null;
    }

    private static byte[] decodeKey(String secret) throws Exception {
        return Base32String.decode(secret);
    }
}

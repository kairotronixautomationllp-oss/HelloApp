# MyChat — Android build package

## Current status

Source updated for email/password sign-in to Firebase project `helloapp-33461`, application ID `com.chandravir.HelloApp` (case sensitive). Use the account you created in Firebase Authentication and its Firebase password. No password is included in this package.

**This archive is source code, not an APK. It has not been compiled or tested on a device.** The preparation environment has Java but no Flutter or Android SDK. Attempts to retrieve Flutter SDK archives returned HTTP 404. The included workflow has not been run.

## Build without installing tools on a computer

1. Create a private GitHub repository.
2. Upload the **contents** of the `MyChat` folder to the repository root, including `.github/workflows/android-apk.yml`. Do not upload just this ZIP or nest the folder under the repository root.
3. Open Actions > Build MyChat APK > Run workflow.
4. After a successful run, download `MyChat-APK` under Artifacts and extract `app-debug.apk`.
5. Transfer it to your Android phone and open the APK to install. This is a development APK for testing, not a Play Store release.

GitHub usage/costs depend on your account. No repository has been created or uploaded by this package.

## Build on a computer

Install Flutter 3.29.3, Python 3, JDK 17 and the Android SDK, then run from this folder:

```
python3 build_apk.py
```

On success, the script creates `MyChat.apk` in this folder. It first generates the Android project, fetches dependencies, analyzes the code, and compiles a debug APK.

## Firebase prerequisites

- Enable Email/Password under Authentication > Sign-in method. An email/password account was visible in the supplied console screenshot; a live login has not been verified.
- Login works independently of Firestore. A failed profile sync displays an error without ending the signed-in session.
- Create Cloud Firestore and publish the **updated** `firestore.rules` before profile discovery and chats. Earlier rules required a phone claim and do not support the new email login profile.
- Create Firebase Storage and publish `storage.rules` before image upload. Billing requirements must be reviewed in your console; no billing changes have been made.
- Friends must have their own Firebase email/password account and sign in once to appear in discovery. Search by their email. Phone discovery only works for an account with a verified linked phone number; phone linking is not implemented here.

## Features and limits

Email/password login, password visibility toggle, password reset request, sign out, friend lookup by email or a linked verified number, text chat and image upload are included in source. Input validation and login errors are handled. Email accounts use Firebase SDK authentication; passwords are not saved by this source.

Device contact sync, SMS login/linking, invitation-only membership, push notifications and video calls are not implemented. The existing discovery rules permit signed-in users to read profiles. Do not treat this starter as a finished private messenger. Rules have not been deployed, and end-to-end authentication/chat/image flows have not been verified.

## Manual verification after build

Install on an Android device. Check invalid credentials, correct login, app restart/session restore, sign out, password visibility and password reset. Then use a second account/device to check discovery, text and image exchange after publishing the rules. A third account must be unable to read another chat's messages.

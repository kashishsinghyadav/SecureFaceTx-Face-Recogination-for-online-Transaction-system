# Face Recognition Transaction System

This project implements face recognition for a transaction system using Keras, OpenCV, data augmentation, and OTP verification with Django as the backend.


```mermaid
graph TD;
    Start --> User_Registration --> Login_Face_Recognition --> Dashboard --> Transaction_Process --> End
    User_Registration --> |Registration Successful| Authentication;
    Authentication --> |Successful| Update;
    Update --> |Transaction Successful| End;
    Login_Face_Recognition --> |Login Successful| Dashboard;
    Login_Face_Recognition --> |Login Failed| User_Registration;
    Dashboard --> |New Transaction| Transaction_Process;
    Transaction_Process --> |Redirect to OTP Verification| OTP_Verification;
    OTP_Verification --> |Successful| Transaction_Process;
    OTP_Verification --> |Failed| End;
    User_Registration --> |Login Failed| End;
    Dashboard --> |Login Failed| User_Registration;
    Transaction_Process --> |Failed| End;
    OTP_Verification --> |Redirect to Login| User_Registration;
    OTP_Verification --> |Redirect to Transaction| Transaction_Process;
```

## Project Srceenshot
<details>
<summary><strong>Screenshots (click to expand)</strong></summary>

<!-- Add your screenshots here -->
## Home Page

![Screenshot 1](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/d59d1454-9b89-4c72-9c3d-17037ae3fc8d)

## Registration Page
    # user register themselves using credential
    ``` 
    faceid(unique),
    Name,
    email,
    address,
    Phone number,
    uploadimage
    ```
![Screenshot (2)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/d0792921-275c-409e-b322-457de0ad799c)


## Login 
    # It done by the real time camera 




    
![Screenshot (26)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/18f6b776-7339-4c91-ae82-3b37e56033ef)


## User Dashboard
    # the specifc user dashboard which user login successfully


![Screenshot (3)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/705dfdbf-0d4a-4ce4-ba12-d1a8ff0e65fe)

 ## User details 
    #  user also update thier details upload their image
    
![Screenshot (24)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/ce521f7e-f24f-4bd5-b3e8-02d1547333b4)


## Transaction Page


![Screenshot (20)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/9b8583b0-3812-413b-a94c-4d22173406bb)





![Screenshot (21)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/5ba486cc-1fb3-4bc6-8173-df7b4e1da1f4)



## OTP Page
    # user enter the register email

![Screenshot (18)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/9a30fc81-65e5-4efc-9ef4-a89da30815a9)

## Verification Page
    # user enter the otp(6 digits) which is send to mail



![Screenshot (22)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/5bc2731c-930e-4497-8ddb-b878a2690457)


## Successful Transaction
    # if otp is authenticate then transaction became succesful

![Screenshot (23)](https://github.com/kashishsinghyadav/SecureFaceTx-Face-Recogination-for-online-Transaction-system/assets/117498422/1ff6548c-81a5-43b9-8ea1-58eabf048230)





<!-- Add more screenshots as needed -->


</details>

## Overview

The Face Recognition Transaction System is designed to enhance security and convenience in financial transactions by implementing a face recognition system. This system verifies the identity of users through their facial features and integrates OTP (One Time Password) verification for additional security.

## Features

- Face recognition using Keras and OpenCV.
- Data augmentation techniques for improving model performance.
- OTP verification for secure transactions.
- User-friendly interface for seamless interaction.
- User perform curd operations to manage their profile

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kashishsinghyadav/Face-Recogination-for-online-transaction-.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the pre-trained model weights for face recognition.

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the Django server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Launch the Django server.
2. Register your face by following the instructions.
3. Initiate a transaction.
4. The system will verify your identity through face recognition.
5. Enter the OTP received on your registered device to complete the transaction.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests to suggest improvements or add new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [kashish ](mailto:kashishhsinghhh@gmail.com).




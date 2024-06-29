# XFI Description

XFI is a tool designed to detect Local File Inclusion (LFI) and Remote File Inclusion (RFI) vulnerabilities in web servers. This tool allows security professionals to evaluate the security posture of their web applications efficiently.

## Context

Local File Inclusion (LFI) and Remote File Inclusion (RFI) are common vulnerabilities in web applications. These vulnerabilities allow attackers to include files on the web server, which can lead to information disclosure, remote code execution, and other malicious activities. XFI aims to help identify these vulnerabilities before they can be exploited by attackers in addition to that, **XFI allows you to test a huge quantity of payloads in a short time.**

## Usage

XFI operates in two main steps:

1. **Configuration Step**: Specify the target and the type of vulnerability you want to evaluate.
2. **Testing Step**: Execute the actual test on the specified target.

### Step 1: Configuration

Run the following command to configure the tool:

```sh
py xfi.py configure
```

This command will prompt you to specify the target web server and the type of vulnerability (LFI or RFI) you want to test for.


### Step 2: Testing

Once the configuration is complete, run the following command to start the test:

```
py xfi.py run
```

This command will execute the test based on the configuration and will output the results, indicating whether the target is vulnerable to LFI or RFI.

## Example

#### Local File inclusion Check

![image](https://github.com/njammy/xfi/assets/109813492/df9184ed-ba97-4a34-8990-0cfc019b9a57)


## MIT License
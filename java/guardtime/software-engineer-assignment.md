# Software Engineer test assignment

> Локальная копия. Источник: <https://github.com/guardtime/software-engineer-assignment>

It is recommended to read the Java SDK documentation ([KSI Java SDK code](https://github.com/GuardTime/ksi-java-sdk)) and examples ([KSI SDK examples](https://github.com/GuardTime/ksi-sdk-samples)) before starting to write any code. Also, access to the [KSI Gateway](https://guardtime.com/technology/blockchain-developers) is required.

## Setup

Clone the template repository to your local machine. When working on the solution, maintain local Git history. When submitting the solution, include the hidden `.git` folder.

While the implementation of the API can be chosen by the candidate, a template is given in this repository with two isolated subprojects:

* `container-library` - implements the API
* `end-user-application` - consumes the API

## Functional requirements

The KSI SDK leaves the safekeeping and storage of the signed file and signature to the customer. Usually, they are kept as two separate files on disk or in the database. In some situations, it would be beneficial to use some other format and one of the simplest solutions would be to use containers.

Your task is to write a container API which:

* allows the creation of containers from existing files
* can open containers created by it
* allows adding new signatures to an existing container
* allows removal of signatures from an existing container

## Structure of the container

The solution should be based on ZIP format. One possible example with three data files and two signatures would look like this:

```text
/datafile1.txt
/datafile2.pdf 
/datafile3.png 
/META-INF/manifest1.tlv 
/META-INF/signature1.ksi 
/META-INF/manifest2.tlv 
/META-INF/signature2.ksi
```

Unlike when signing a single file, in case of containers, one does not sign the hash(es) of the data file(es).
Instead, the intermediate structures, containing the data file(s) hash(es), are being signed.
The files `/META-INF/manifest1.tlv` and `/META-INF/manifest2.tlv` are such intermediate structures (in the further text referred as “manifest”) for the signatures `/META-INF/signature1.ksi` and `/META-INF/signature2.ksi`.

Manifest contains the URI and hash (together with algorithm reference) for each connected data file. Additionally, it contains the URI for the signature.
This manifest is then signed. For each new signature, a new manifest is created. An abstract example of a structure for the manifest:

```text
datafile
    uri= datafile1.txt
    hashalgorithm=SHA256
    hash=...
datafile
    uri= datafile2.pdf
    hashalgorithm=SHA512
    hash=...
signature-uri=/METAINF/signature1.ksi
```

While you can choose the format for the manifest file for yourself, it is recommended to use TLV format. The lower levels of the Java SDK should give you tools for that.

## Non-functional requirements

* Use either Maven or Gradle
* All public classes and interfaces should be documented according to Google Java Style. No extensive documentation is needed.
* The solution has to include a user guide.
* The solution must use as few third-party libraries as possible. Each such use must be justified.
* The solution must accept large data files (2-3GB).
* The solution must accept a large number of input files (10000).
* The solution must be covered by the unit and integration tests.
* Delivery must include the source & `.git` directory together with documentation and tests.

## Hints

<details>
    <summary>1. Container structure</summary>

The container can be thought of as the Estonian digital signature container (`*.asice`). When implementing the API, one may draw ideas from the functionalities that the DigiDoc client offers.

Articles to read that may bring clarity:

1. [BDOC file format](https://www.id.ee/en/article/bdoc-file-format/), the article also contains reference to BDOC format specification
2. [What is the difference between digitally signed documents with .bdoc and .asice extensions?](https://www.id.ee/en/article/what-is-the-difference-between-digitally-signed-documents-with-bdoc-and-asice-extensions/)

</details>

<details>
    <summary>2. TLV element creation</summary>

SDK class [com.guardtime.ksi.tlv.TlvElement](https://guardtime.github.io/ksi-java-sdk/com/guardtime/ksi/tlv/TLVElement.html) can be used for creation of the TLV elements.

SDK class [com.guardtime.ksi.hashing.DataHasher](https://guardtime.github.io/ksi-java-sdk/com/guardtime/ksi/hashing/DataHasher.html) can be used for calculating hashes of the input file(s).
</details>

<details>
    <summary>3. KSI signing client setup</summary>

`ksi-sdk-samples` repository contains a [demonstration](https://github.com/guardtime/ksi-sdk-samples/blob/master/java-sdk/src/test/java/com/guardtime/ksi/samples/KsiSamples.java#L101) on how to set up the KSI signing client.
</details>

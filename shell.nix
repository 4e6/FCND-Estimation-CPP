with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "backyard-flyer-env";
  buildInputs = [
    # these packages are required for virtualenv and pip to work:
    python3Full
    # python libs
    python3Packages.numpy
  ];

  src = null;

  LANG = "en_US.UTF-8";
}

{ pkgs ? import <nixpkgs> {} }:

with pkgs;

stdenv.mkDerivation {
  name = "aurproxy";
  buildInputs = [ python2 python2Packages.virtualenv libffi openssl ];
  shellHook = ''
    unset SOURCE_DATE_EPOCH;
  '';
}

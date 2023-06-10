
resource "oci_identity_compartment" "tf-compartment" {
    # Required
    compartment_id = var.compartment_ocid
    description = "Compartment for Terraform resources."
    name = "Homelab-02"
}

variable "compartment_ocid" {}
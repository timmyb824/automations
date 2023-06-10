resource "oci_core_instance" "ubuntu_instance" {
  # Required
  availability_domain = data.oci_identity_availability_domains.ads.availability_domains[0].name
  compartment_id      = var.compartment_ocid
  shape               = "VM.Standard.E2.1.Micro"
  source_details {
    source_id   = var.image_ocid
    source_type = "image"
  }

  # Optional
  display_name = "homelab-demo-ubuntu"
  create_vnic_details {
    assign_public_ip = true
    subnet_id        = var.subnet_id
  }
  metadata = {
    ssh_authorized_keys = file("~/.ssh/id_master_key.pub")
  }
  preserve_boot_volume = false
}


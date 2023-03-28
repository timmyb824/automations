resource "cloudflare_record" "terraform_managed_resource_a_0" {
  name    = var.domain
  proxied = true
  ttl     = 1
  type    = "A"
  value   = var.ip_address
  zone_id = var.zone_id
}

resource "cloudflare_record" "terraform_managed_resource_cname_0" {
  name    = "_domainconnect"
  proxied = true
  ttl     = 1
  type    = "CNAME"
  value   = "connect.domains.google.com"
  zone_id = var.zone_id
}

resource "cloudflare_record" "terraform_managed_resource_cname_1" {
  name    = "hass"
  proxied = true
  ttl     = 1
  type    = "CNAME"
  value   = var.domain
  zone_id = var.zone_id
}

resource "cloudflare_record" "terraform_managed_resource_cname_2" {
  name    = "npm"
  proxied = true
  ttl     = 1
  type    = "CNAME"
  value   = var.domain
  zone_id = var.zone_id
}

resource "cloudflare_record" "terraform_managed_resource_cname_3" {
  name    = "pve"
  proxied = true
  ttl     = 1
  type    = "CNAME"
  value   = var.domain
  zone_id = var.zone_id
}

resource "cloudflare_record" "terraform_managed_resource_cname_4" {
  name    = "www"
  proxied = true
  ttl     = 1
  type    = "CNAME"
  value   = var.domain
  zone_id = var.zone_id
}


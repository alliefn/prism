# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contributors(models.Model):
    _name = 'contributors.contrib'
    _description = 'Deskripsi Kontributor Chempro'


    name = fields.Char(string="Nama", required=True)
    nim = fields.Char(string="NIM", required=True)
    tarif = fields.Char(string="Tarif")
    contact = fields.Char(string="Kontak", required=True)
    achievement = fields.Char(string="Prestasi")
    contribution = fields.Char(string="Kontribusi")

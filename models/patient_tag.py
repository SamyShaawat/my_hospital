from odoo import api, fields, models, _


class PatientTag(models.Model):
    _name = 'patient.tag'
    _inherit = ['mail.thread']
    _description = 'Patient Tag'
    name = fields.Char(string='Name', required=True, tracking=True)

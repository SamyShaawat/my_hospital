from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'
    name = fields.Char(string='Name', required=True, tracking=True)
    date_of_birth = fields.Datetime(string='DOB', tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string='Gender', tracking=True)
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string='Tags')

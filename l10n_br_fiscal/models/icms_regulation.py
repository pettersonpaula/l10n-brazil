# Copyright (C) 2019  Renato Lima - Akretion <renato.lima@akretion.com.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from lxml import etree

from odoo import api, fields, models

from ..constants.fiscal import (
    TAX_DOMAIN_ICMS,
    TAX_DOMAIN_ICMS_ST,
    TAX_DOMAIN_ICMS_FCP
)

VIEW = """
<page name="uf_{0}" string="{1}">
    <notebook>
        <page name="uf_{0}_internal" string="Interno">
            <group name="icms_internal_{0}" string="Internal">
            <field name="icms_internal_{0}_ids" context="{{'tree_view_ref': 'l10n_br_fiscal.tax_definition_icms_tree', 'default_icms_regulation_id': id, 'default_tax_group_id': {2}, 'default_state_from_id': {5}, 'default_state_to_id': {5}}}"/>
            </group>
            <group name="icms_external_{0}" string="External">
            <field name="icms_external_{0}_ids" context="{{'tree_view_ref': 'l10n_br_fiscal.tax_definition_icms_tree', 'default_icms_regulation_id': id, 'default_tax_group_id': {2}, 'default_state_from_id': {5}}}"/>
            </group>
        </page>
        <page name="uf_{0}_st" string="ST">
            <field name="icms_st_{0}_ids" context="{{'tree_view_ref': 'l10n_br_fiscal.tax_definition_icms_tree', 'default_icms_regulation_id': id, 'default_tax_group_id': {3}, 'default_state_from_id': {5}, 'default_state_to_id': {5}}}"/>
        </page>
        <page name="uf_{0}_others" string="Outros">
            <field name="icms_fcp_{0}_ids" context="{{'tree_view_ref': 'l10n_br_fiscal.tax_definition_icms_tree', 'default_icms_regulation_id': id, 'default_tax_group_id': {4}, 'default_state_from_id': {5}, 'default_state_to_id': {5}}}"/>
        </page>
    </notebook>
</page>
"""  # noqa


class ICMSRegulation(models.Model):
    _name = 'l10n_br_fiscal.icms.regulation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tax ICMS Regulation'

    name = fields.Text(
        string='Name',
        required=True,
        index=True)

    icms_imported_tax_id = fields.Many2one(
        comodel_name='l10n_br_fiscal.tax',
        string='ICMS Tax Imported',
        domain=[('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_internal_ac_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal AC',
        domain=[('state_from_id.code', '=', 'AC'),
                ('state_to_id.code', '=', 'AC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_ac_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External AC',
        domain=[('state_from_id.code', '=', 'AC'),
                ('state_to_id.code', '!=', 'AC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_ac_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST AC',
        domain=[('state_from_id.code', '=', 'AC'),
                ('state_to_id.code', '=', 'AC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_ac_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP AC',
        domain=[('state_from_id.code', '=', 'AC'),
                ('state_to_id.code', '=', 'AC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_al_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal AL',
        domain=[('state_from_id.code', '=', 'AL'),
                ('state_to_id.code', '=', 'AL'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_al_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External AL',
        domain=[('state_from_id.code', '=', 'AL'),
                ('state_to_id.code', '!=', 'AL'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_al_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST AL',
        domain=[('state_from_id.code', '=', 'AL'),
                ('state_to_id.code', '=', 'AL'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_al_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP AL',
        domain=[('state_from_id.code', '=', 'AL'),
                ('state_to_id.code', '=', 'AL'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_am_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal AM',
        domain=[('state_from_id.code', '=', 'AM'),
                ('state_to_id.code', '=', 'AM'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_am_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External AM',
        domain=[('state_from_id.code', '=', 'AM'),
                ('state_to_id.code', '!=', 'AM'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_am_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST AM',
        domain=[('state_from_id.code', '=', 'AM'),
                ('state_to_id.code', '=', 'AM'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_am_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP AM',
        domain=[('state_from_id.code', '=', 'AM'),
                ('state_to_id.code', '=', 'AM'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_ap_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal AP',
        domain=[('state_from_id.code', '=', 'AP'),
                ('state_to_id.code', '=', 'AP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_ap_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External AP',
        domain=[('state_from_id.code', '=', 'AP'),
                ('state_to_id.code', '!=', 'AP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_ap_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST AP',
        domain=[('state_from_id.code', '=', 'AP'),
                ('state_to_id.code', '=', 'AP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_ap_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP AP',
        domain=[('state_from_id.code', '=', 'AP'),
                ('state_to_id.code', '=', 'AP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_ba_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal BA',
        domain=[('state_from_id.code', '=', 'BA'),
                ('state_to_id.code', '=', 'BA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_ba_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External BA',
        domain=[('state_from_id.code', '=', 'BA'),
                ('state_to_id.code', '!=', 'BA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_ba_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST BA',
        domain=[('state_from_id.code', '=', 'BA'),
                ('state_to_id.code', '=', 'BA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_ba_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP BA',
        domain=[('state_from_id.code', '=', 'BA'),
                ('state_to_id.code', '=', 'BA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_ce_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal CE',
        domain=[('state_from_id.code', '=', 'CE'),
                ('state_to_id.code', '=', 'CE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_ce_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External CE',
        domain=[('state_from_id.code', '=', 'CE'),
                ('state_to_id.code', '!=', 'CE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_ce_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST CE',
        domain=[('state_from_id.code', '=', 'CE'),
                ('state_to_id.code', '=', 'CE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_ce_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP CE',
        domain=[('state_from_id.code', '=', 'CE'),
                ('state_to_id.code', '=', 'CE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_df_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal DF',
        domain=[('state_from_id.code', '=', 'DF'),
                ('state_to_id.code', '=', 'DF'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_df_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External DF',
        domain=[('state_from_id.code', '=', 'DF'),
                ('state_to_id.code', '!=', 'DF'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_df_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST DF',
        domain=[('state_from_id.code', '=', 'DF'),
                ('state_to_id.code', '=', 'DF'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_df_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP DF',
        domain=[('state_from_id.code', '=', 'DF'),
                ('state_to_id.code', '=', 'DF'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_es_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal ES',
        domain=[('state_from_id.code', '=', 'ES'),
                ('state_to_id.code', '=', 'ES'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_es_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External ES',
        domain=[('state_from_id.code', '=', 'ES'),
                ('state_to_id.code', '!=', 'ES'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_es_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST ES',
        domain=[('state_from_id.code', '=', 'ES'),
                ('state_to_id.code', '=', 'ES'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_es_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP ES',
        domain=[('state_from_id.code', '=', 'ES'),
                ('state_to_id.code', '=', 'ES'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_go_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal GO',
        domain=[('state_from_id.code', '=', 'GO'),
                ('state_to_id.code', '=', 'GO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_go_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External GO',
        domain=[('state_from_id.code', '=', 'GO'),
                ('state_to_id.code', '!=', 'GO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_go_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST GO',
        domain=[('state_from_id.code', '=', 'GO'),
                ('state_to_id.code', '=', 'GO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_go_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP GO',
        domain=[('state_from_id.code', '=', 'GO'),
                ('state_to_id.code', '=', 'GO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_ma_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal MA',
        domain=[('state_from_id.code', '=', 'MA'),
                ('state_to_id.code', '=', 'MA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_ma_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External MA',
        domain=[('state_from_id.code', '=', 'MA'),
                ('state_to_id.code', '!=', 'MA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_ma_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST MA',
        domain=[('state_from_id.code', '=', 'MA'),
                ('state_to_id.code', '=', 'MA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_ma_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP MA',
        domain=[('state_from_id.code', '=', 'MA'),
                ('state_to_id.code', '=', 'MA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_mt_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal MT',
        domain=[('state_from_id.code', '=', 'MT'),
                ('state_to_id.code', '=', 'MT'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_mt_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External MT',
        domain=[('state_from_id.code', '=', 'MT'),
                ('state_to_id.code', '!=', 'MT'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_mt_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST MT',
        domain=[('state_from_id.code', '=', 'MT'),
                ('state_to_id.code', '=', 'MT'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_mt_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP MT',
        domain=[('state_from_id.code', '=', 'MT'),
                ('state_to_id.code', '=', 'MT'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_ms_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal MS',
        domain=[('state_from_id.code', '=', 'MS'),
                ('state_to_id.code', '=', 'MS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_ms_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External MS',
        domain=[('state_from_id.code', '=', 'MS'),
                ('state_to_id.code', '!=', 'MS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_ms_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST MS',
        domain=[('state_from_id.code', '=', 'MS'),
                ('state_to_id.code', '=', 'MS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_ms_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP MS',
        domain=[('state_from_id.code', '=', 'MS'),
                ('state_to_id.code', '=', 'MS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_mg_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal MG',
        domain=[('state_from_id.code', '=', 'MG'),
                ('state_to_id.code', '=', 'MG'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_mg_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External MG',
        domain=[('state_from_id.code', '=', 'MG'),
                ('state_to_id.code', '!=', 'MG'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_mg_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST MG',
        domain=[('state_from_id.code', '=', 'MG'),
                ('state_to_id.code', '=', 'MG'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_mg_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP MG',
        domain=[('state_from_id.code', '=', 'MG'),
                ('state_to_id.code', '=', 'MG'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_pa_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal PA',
        domain=[('state_from_id.code', '=', 'PA'),
                ('state_to_id.code', '=', 'PA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_pa_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External PA',
        domain=[('state_from_id.code', '=', 'PA'),
                ('state_to_id.code', '!=', 'PA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_pa_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST PA',
        domain=[('state_from_id.code', '=', 'PA'),
                ('state_to_id.code', '=', 'PA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_pa_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP PA',
        domain=[('state_from_id.code', '=', 'PA'),
                ('state_to_id.code', '=', 'PA'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_pb_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal PB',
        domain=[('state_from_id.code', '=', 'PB'),
                ('state_to_id.code', '=', 'PB'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_pb_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External PB',
        domain=[('state_from_id.code', '=', 'PB'),
                ('state_to_id.code', '!=', 'PB'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_pb_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST PB',
        domain=[('state_from_id.code', '=', 'PB'),
                ('state_to_id.code', '=', 'PB'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_pb_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP PB',
        domain=[('state_from_id.code', '=', 'PB'),
                ('state_to_id.code', '=', 'PB'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_pr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal PR',
        domain=[('state_from_id.code', '=', 'PR'),
                ('state_to_id.code', '=', 'PR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_pr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External PR',
        domain=[('state_from_id.code', '=', 'PR'),
                ('state_to_id.code', '!=', 'PR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_pr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST PR',
        domain=[('state_from_id.code', '=', 'PR'),
                ('state_to_id.code', '=', 'PR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_pr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP PR',
        domain=[('state_from_id.code', '=', 'PR'),
                ('state_to_id.code', '=', 'PR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_pe_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal PE',
        domain=[('state_from_id.code', '=', 'PE'),
                ('state_to_id.code', '=', 'PE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_pe_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External PE',
        domain=[('state_from_id.code', '=', 'PE'),
                ('state_to_id.code', '!=', 'PE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_pe_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST PE',
        domain=[('state_from_id.code', '=', 'PE'),
                ('state_to_id.code', '=', 'PE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_pe_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP PE',
        domain=[('state_from_id.code', '=', 'PE'),
                ('state_to_id.code', '=', 'PE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_pi_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal PI',
        domain=[('state_from_id.code', '=', 'PI'),
                ('state_to_id.code', '=', 'PI'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_pi_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External PI',
        domain=[('state_from_id.code', '=', 'PI'),
                ('state_to_id.code', '!=', 'PI'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_pi_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST PI',
        domain=[('state_from_id.code', '=', 'PI'),
                ('state_to_id.code', '=', 'PI'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_pi_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP PI',
        domain=[('state_from_id.code', '=', 'PI'),
                ('state_to_id.code', '=', 'PI'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_rn_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal RN',
        domain=[('state_from_id.code', '=', 'RN'),
                ('state_to_id.code', '=', 'RN'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_rn_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External RN',
        domain=[('state_from_id.code', '=', 'RN'),
                ('state_to_id.code', '!=', 'RN'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_rn_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST RN',
        domain=[('state_from_id.code', '=', 'RN'),
                ('state_to_id.code', '=', 'RN'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_rn_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP RN',
        domain=[('state_from_id.code', '=', 'RN'),
                ('state_to_id.code', '=', 'RN'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_rs_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal RS',
        domain=[('state_from_id.code', '=', 'RS'),
                ('state_to_id.code', '=', 'RS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_rs_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External RS',
        domain=[('state_from_id.code', '=', 'RS'),
                ('state_to_id.code', '!=', 'RS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_rs_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST RS',
        domain=[('state_from_id.code', '=', 'RS'),
                ('state_to_id.code', '=', 'RS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_rs_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP RS',
        domain=[('state_from_id.code', '=', 'RS'),
                ('state_to_id.code', '=', 'RS'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_rj_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal RJ',
        domain=[('state_from_id.code', '=', 'RJ'),
                ('state_to_id.code', '=', 'RJ'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_rj_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External RJ',
        domain=[('state_from_id.code', '=', 'RJ'),
                ('state_to_id.code', '!=', 'RJ'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_rj_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST RJ',
        domain=[('state_from_id.code', '=', 'RJ'),
                ('state_to_id.code', '=', 'RJ'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_rj_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP RJ',
        domain=[('state_from_id.code', '=', 'RJ'),
                ('state_to_id.code', '=', 'RJ'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_ro_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal RO',
        domain=[('state_from_id.code', '=', 'RO'),
                ('state_to_id.code', '=', 'RO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_ro_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External RO',
        domain=[('state_from_id.code', '=', 'RO'),
                ('state_to_id.code', '!=', 'RO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_ro_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST RO',
        domain=[('state_from_id.code', '=', 'RO'),
                ('state_to_id.code', '=', 'RO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_ro_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP RO',
        domain=[('state_from_id.code', '=', 'RO'),
                ('state_to_id.code', '=', 'RO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_rr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal RR',
        domain=[('state_from_id.code', '=', 'RR'),
                ('state_to_id.code', '=', 'RR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_rr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External RR',
        domain=[('state_from_id.code', '=', 'RR'),
                ('state_to_id.code', '!=', 'RR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_rr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST RR',
        domain=[('state_from_id.code', '=', 'RR'),
                ('state_to_id.code', '=', 'RR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_rr_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP RR',
        domain=[('state_from_id.code', '=', 'RR'),
                ('state_to_id.code', '=', 'RR'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_sc_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal SC',
        domain=[('state_from_id.code', '=', 'SC'),
                ('state_to_id.code', '=', 'SC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_sc_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External SC',
        domain=[('state_from_id.code', '=', 'SC'),
                ('state_to_id.code', '!=', 'SC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_sc_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST SC',
        domain=[('state_from_id.code', '=', 'SC'),
                ('state_to_id.code', '=', 'SC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_sc_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP SC',
        domain=[('state_from_id.code', '=', 'SC'),
                ('state_to_id.code', '=', 'SC'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_sp_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal SP',
        domain=[('state_from_id.code', '=', 'SP'),
                ('state_to_id.code', '=', 'SP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_sp_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External SP',
        domain=[('state_from_id.code', '=', 'SP'),
                ('state_to_id.code', '!=', 'SP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_sp_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST SP',
        domain=[('state_from_id.code', '=', 'SP'),
                ('state_to_id.code', '=', 'SP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_sp_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP SP',
        domain=[('state_from_id.code', '=', 'SP'),
                ('state_to_id.code', '=', 'SP'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_se_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal SE',
        domain=[('state_from_id.code', '=', 'SE'),
                ('state_to_id.code', '=', 'SE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_se_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External SE',
        domain=[('state_from_id.code', '=', 'SE'),
                ('state_to_id.code', '!=', 'SE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_se_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST SE',
        domain=[('state_from_id.code', '=', 'SE'),
                ('state_to_id.code', '=', 'SE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_se_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP SE',
        domain=[('state_from_id.code', '=', 'SE'),
                ('state_to_id.code', '=', 'SE'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    icms_internal_to_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS Internal TO',
        domain=[('state_from_id.code', '=', 'TO'),
                ('state_to_id.code', '=', 'TO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_external_to_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS External TO',
        domain=[('state_from_id.code', '=', 'TO'),
                ('state_to_id.code', '!=', 'TO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS)])

    icms_st_to_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS ST TO',
        domain=[('state_from_id.code', '=', 'TO'),
                ('state_to_id.code', '=', 'TO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_ST)])

    icms_fcp_to_ids = fields.One2many(
        comodel_name='l10n_br_fiscal.tax.definition',
        inverse_name='icms_regulation_id',
        string='ICMS FCP TO',
        domain=[('state_from_id.code', '=', 'TO'),
                ('state_to_id.code', '=', 'TO'),
                ('tax_group_id.tax_domain', '=', TAX_DOMAIN_ICMS_FCP)])

    @api.model
    def fields_view_get(self, view_id=None, view_type='form',
                        toolbar=False, submenu=False):

        view_super = super(ICMSRegulation, self).fields_view_get(
            view_id, view_type, toolbar, submenu)

        if view_type == 'form':
            doc = etree.fromstring(view_super.get('arch'))

            for node in doc.xpath("//notebook"):

                br_states = self.env['res.country.state'].search(
                    [('country_id', '=', self.env.ref('base.br').id)],
                    order="code")

                i = 0
                for state in br_states:
                    i += 1
                    state_page = VIEW.format(
                        state.code.lower(),
                        state.name,
                        self.env.ref('l10n_br_fiscal.tax_group_icms').id,
                        self.env.ref('l10n_br_fiscal.tax_group_icmsst').id,
                        self.env.ref('l10n_br_fiscal.tax_group_icmsfcp').id,
                        state.id)
                    node_page = etree.fromstring(state_page)
                    node.insert(i, node_page)

            view_super['arch'] = etree.tostring(doc, encoding='unicode')

        return view_super

    @api.multi
    def map_tax_icms(self, company, partner, product, ncm=None,
                     cest=None, operation_line=None):

        self.ensure_one()
        tax_definitions = self.env['l10n_br_fiscal.tax.definition']
        tax_group_icms = self.env.ref('l10n_br_fiscal.tax_group_icms')
        tax_group_icmsst = self.env.ref('l10n_br_fiscal.tax_group_icmsst')
        # tax_group_icmsfcp = self.env.ref('l10n_br_fiscal.tax_group_icmsfcp')

        if not ncm:
            ncm = product.ncm_id

        if not cest:
            cest = product.cest_id

        domain = [
            ('icms_regulation_id', '=', self.id),
            ('state_from_id', '=', company.state_id.id),
        ]

        # Is Partner ICMS Taxpayer?
        # ICMS
        icms_domain = domain
        if partner.is_company:
            icms_domain.append(('state_to_id', '=', partner.state_id.id))
        else:
            icms_domain.append(('state_to_id', '=', company.state_id.id))

        icms_domain.append(('tax_group_id', '=', tax_group_icms.id))

        tax_definitions |= tax_definitions.search(icms_domain)

        # ICMS ST
        icmsst_domain = domain
        icmsst_domain += [
            '|',
            ('state_to_id', '=', partner.state_id.id),
            ('state_to_id', '=', company.state_id.id)]

        icmsst_domain.append(('tax_group_id', '=', tax_group_icmsst.id))
        icmsst_domain.append(('ncm_ids', '=', ncm.id))
        icmsst_domain.append(('cest_ids', '=', cest.id))

        tax_definitions |= tax_definitions.search(icmsst_domain)

        return tax_definitions.mapped('tax_id')

    def _map_icms_origin(self, company, partner, product, ncm=None,
                         cest=None, operation_line=None):
        pass

    def _map_icms_destination(self, company, partner, product, ncm=None,
                              cest=None, operation_line=None):
        pass

    def _map_icmsst(self, company, partner, product, ncm=None,
                    cest=None, operation_line=None):
        pass

    def _map_icmsfcp(self, company, partner, product, ncm=None,
                     cest=None, operation_line=None):
        pass

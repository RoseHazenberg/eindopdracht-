#!/usr/bin/env python3


"""This script describes the process meiose 1 with crossing-over
that is needed to make a animation"""

__author__ = "Rose Hazenberg and Akastia Christo"
__version__ = "1.0"

from pypovray import pypovray, models
from vapory import Scene, Sphere, Cylinder, Text, LightSource
from vapory import Texture, Pigment, Finish, Union, Intersection, Interior, Material, Box


CL_NUC = Material(Texture(Pigment('color', [1, 0.7, 1], 'filter', 0.7)), Interior('ior', 1.0))
CL_BASE = Material(Texture(Pigment('color', [1, 1, 1], 'filter', 0.7)), Interior('ior', 1.0))
CL_BASE_1 = Material(Texture(Pigment('color', [1, 1, 1], 'filter', 0)))
CL_B = Texture(Pigment('color', [0, 1, 1]))
CL_P = Texture(Pigment('color', [1, 0, 1]))
CL_R = Texture(Pigment('color', [1, 0, 0]), Finish('phong', 0.6))


def make_meiose_base(x_pos, y_pos, z_pos, straal):
    """This is the cel for the start of the animation"""
    meiose_base = Sphere([x_pos, y_pos, z_pos], straal, CL_BASE_1)
    meiose_base_n = Sphere([0, 0, 0], 0, CL_BASE_1)
    return meiose_base, meiose_base_n


def make_meiose_trans():
    """This is the cell with the nucleus"""
    base = Sphere([0, 5, 0], 5, CL_BASE, 'no_shadow')
    nucleus = Sphere([2, 5, 0], 2, CL_NUC, 'no_shadow')
    return base, nucleus


def zoom_nuc_base_in(x_pos, y_pos, z_pos):
    """This is the zooomed cell with the nucleus for prophase untill the end"""
    base = Sphere([-2, 3, 4], 8, CL_BASE, 'translate', [x_pos, y_pos, z_pos+4], 'no_shadow')
    nuc = Sphere([-1, 5, 0], 4, CL_NUC, 'translate', [x_pos, y_pos, z_pos], 'no_shadow')
    return nuc, base


def zoom_base_in(x_pos, y_pos, z_pos):
    """This is the zoomed cell when the nucleus disappears"""
    zoom_nuc = Sphere([0, 0, 0], 0, CL_BASE, 'translate', [x_pos, y_pos, z_pos], 'no_shadow')
    zoom_base = Sphere([-2, 3, 4], 8, CL_BASE, 'translate', [x_pos, y_pos, z_pos+4], 'no_shadow')
    return zoom_base, zoom_nuc


def make_chromosome_b(x_pos, y_pos, z_pos, straal):
    """This is for the chromosomes with the color blue"""
    c_l_b_b = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+2, z_pos], straal, CL_B, 'no_shadow')
    c_r_b_b = Cylinder([x_pos+2, y_pos, z_pos], [x_pos+2, y_pos+2, z_pos], straal, CL_B,
                       'no_shadow')
    c_l_o_b = Cylinder([x_pos, y_pos-3, z_pos], [x_pos, y_pos-1, z_pos], straal, CL_B, 'no_shadow')
    c_r_o_b = Cylinder([x_pos+2, y_pos-3, z_pos], [x_pos+2, y_pos-1, z_pos], straal, CL_B,
                       'no_shadow')
    c_l_s_b = Cylinder([x_pos, y_pos+0.2, z_pos], [x_pos+2, y_pos-1.225, z_pos], straal, CL_B,
                       'no_shadow')
    c_r_s_b = Cylinder([x_pos+2, y_pos+0.2, z_pos], [x_pos, y_pos-1.225, z_pos], straal, CL_B,
                       'no_shadow')
    return c_l_b_b, c_r_b_b, c_l_o_b, c_r_o_b, c_l_s_b, c_r_s_b


def make_chromosome_p(x_pos, y_pos, z_pos, straal):
    """This is for the chromosomes with the color purple"""
    c_l_b_p = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+2, z_pos], straal, CL_P, 'no_shadow')
    c_r_b_p = Cylinder([x_pos+2, y_pos, z_pos], [x_pos+2, y_pos+2, z_pos], straal, CL_P,
                       'no_shadow')
    c_l_o_p = Cylinder([x_pos, y_pos-3, z_pos], [x_pos, y_pos-1, z_pos], straal, CL_P, 'no_shadow')
    c_r_o_p = Cylinder([x_pos+2, y_pos-3, z_pos], [x_pos+2, y_pos-1, z_pos], straal, CL_P,
                       'no_shadow')
    c_l_s_p = Cylinder([x_pos, y_pos+0.2, z_pos], [x_pos+2, y_pos-1.225, z_pos], straal, CL_P,
                       'no_shadow')
    c_r_s_p = Cylinder([x_pos+2, y_pos+0.2, z_pos], [x_pos, y_pos-1.225, z_pos], straal, CL_P,
                       'no_shadow')
    return c_l_b_p, c_r_b_p, c_l_o_p, c_r_o_p, c_l_s_p, c_r_s_p


def make_crossing_chromosome_p(x_pos, y_pos, z_pos, straal):
    """This is for the chromosomes when the crossing-over takes place with the color purple"""
    cr_l_b_p = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+2, z_pos], straal, CL_P, 'no_shadow')
    cr_r_b_p = Cylinder([x_pos+2, y_pos, z_pos], [x_pos+2, y_pos+2, z_pos], straal, CL_P,
                        'no_shadow')
    cr_l_o_p = Cylinder([x_pos, y_pos-2, z_pos], [x_pos, y_pos-1, z_pos], straal, CL_P, 'no_shadow')
    cr_r_o_p = Cylinder([x_pos+2, y_pos-3, z_pos], [x_pos+2, y_pos-1, z_pos], straal, CL_P,
                        'no_shadow')
    cr_l_s_p = Cylinder([x_pos, y_pos+0.2, z_pos], [x_pos+2, y_pos-1.225, z_pos], straal, CL_P,
                        'no_shadow')
    cr_r_s_p = Cylinder([x_pos+2, y_pos+0.2, z_pos], [x_pos, y_pos-1.225, z_pos], straal, CL_P,
                        'no_shadow')
    return cr_l_b_p, cr_r_b_p, cr_l_o_p, cr_r_o_p, cr_l_s_p, cr_r_s_p


def make_crossing_chromosome_b(x_pos, y_pos, z_pos, straal):
    """This is for the chromosomes when the crossing-over takes place with the color blue"""
    cr_l_b_b = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+2, z_pos], straal, CL_B, 'no_shadow')
    cr_r_b_b = Cylinder([x_pos+2, y_pos, z_pos], [x_pos+2, y_pos+2, z_pos], straal, CL_B,
                        'no_shadow')
    cr_l_o_b = Cylinder([x_pos, y_pos-2, z_pos], [x_pos, y_pos-1, z_pos], straal, CL_B, 'no_shadow')
    cr_r_o_b = Cylinder([x_pos+2, y_pos-3, z_pos], [x_pos+2, y_pos-1, z_pos], straal, CL_B,
                        'no_shadow')
    cr_l_s_b = Cylinder([x_pos, y_pos+0.2, z_pos], [x_pos+2, y_pos-1.225, z_pos], straal, CL_B,
                        'no_shadow')
    cr_r_s_b = Cylinder([x_pos+2, y_pos+0.2, z_pos], [x_pos, y_pos-1.225, z_pos], straal, CL_B,
                        'no_shadow')
    return cr_l_b_b, cr_r_b_b, cr_l_o_b, cr_r_o_b, cr_l_s_b, cr_r_s_b


def make_crossing_prophase(x_pos, y_pos, z_pos, straal):
    """This is the crossing-over for the prophase"""
    cross_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+1, z_pos], straal, CL_B, 'no_shadow')
    cross_2 = Cylinder([x_pos+0.5, y_pos, z_pos+1], [x_pos+0.5, y_pos+1, z_pos+1], straal, CL_P,
                       'no_shadow')
    cross_3 = Cylinder([x_pos+4, y_pos, z_pos], [x_pos+4, y_pos+1, z_pos], straal, CL_B,
                       'no_shadow')
    cross_4 = Cylinder([x_pos+4.7, y_pos, z_pos+1], [x_pos+4.7, y_pos+1, z_pos+1], straal, CL_P,
                       'no_shadow')
    return cross_1, cross_2, cross_3, cross_4


def make_crossing_metaphase(x_pos, y_pos, z_pos, straal):
    """This is the crossing-over for the metaphase"""
    cross_m_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+1, z_pos], straal, CL_B, 'no_shadow')
    cross_m_2 = Cylinder([x_pos+0.5, y_pos, z_pos+1], [x_pos+0.5, y_pos+1, z_pos+1], straal, CL_P,
                         'no_shadow')
    cross_m_3 = Cylinder([x_pos, y_pos+6, z_pos], [x_pos, y_pos+7, z_pos], straal, CL_B,
                         'no_shadow')
    cross_m_4 = Cylinder([x_pos+0.5, y_pos+6, z_pos+1], [x_pos+0.5, y_pos+7, z_pos+1], straal, CL_P,
                         'no_shadow')
    return cross_m_1, cross_m_2, cross_m_3, cross_m_4


def make_crossing_anaphase(x_pos, y_pos, z_pos, straal):
    """This is the crossing-over for the anaphase"""
    cross_a_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+1, z_pos], straal, CL_B, 'no_shadow')
    cross_a_2 = Cylinder([x_pos+6, y_pos, z_pos], [x_pos+6, y_pos+1, z_pos], straal, CL_P,
                         'no_shadow')
    cross_a_3 = Cylinder([x_pos, y_pos+6, z_pos], [x_pos, y_pos+7, z_pos], straal, CL_B,
                         'no_shadow')
    cross_a_4 = Cylinder([x_pos+6, y_pos+6, z_pos], [x_pos+6, y_pos+7, z_pos], straal, CL_P,
                         'no_shadow')
    return cross_a_1, cross_a_2, cross_a_3, cross_a_4


def make_crossing_telophase(x_pos, y_pos, z_pos, straal):
    """This is the crossing-over for the telophase"""
    cross_t_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+1, z_pos], straal, CL_B, 'no_shadow')
    cross_t_2 = Cylinder([x_pos+11, y_pos, z_pos], [x_pos+11, y_pos+1, z_pos], straal, CL_P,
                         'no_shadow')
    cross_t_3 = Cylinder([x_pos, y_pos+6, z_pos], [x_pos, y_pos+7, z_pos], straal, CL_B,
                         'no_shadow')
    cross_t_4 = Cylinder([x_pos+11, y_pos+6, z_pos], [x_pos+11, y_pos+7, z_pos], straal, CL_P,
                         'no_shadow')
    return cross_t_1, cross_t_2, cross_t_3, cross_t_4


def make_crossing_telophase_3(x_pos, y_pos, z_pos, straal):
    """This is the crossing-over for the telophase part 3"""
    cross_t_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+1, z_pos], straal, CL_B, 'no_shadow')
    cross_t_2 = Cylinder([x_pos+17, y_pos, z_pos], [x_pos+17, y_pos+1, z_pos], straal, CL_P,
                         'no_shadow')
    cross_t_3 = Cylinder([x_pos, y_pos+6, z_pos], [x_pos, y_pos+7, z_pos], straal, CL_B,
                         'no_shadow')
    cross_t_4 = Cylinder([x_pos+17, y_pos+6, z_pos], [x_pos+17, y_pos+7, z_pos], straal, CL_P,
                         'no_shadow')
    return cross_t_1, cross_t_2, cross_t_3, cross_t_4



def make_crossing_cytokinesis(x_pos, y_pos, z_pos, straal):
    """This is the crossing-over for the cytokinesis"""
    cross_c_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+1, z_pos], straal, CL_B, 'no_shadow')
    cross_c_2 = Cylinder([x_pos+22, y_pos, z_pos], [x_pos+22, y_pos+1, z_pos], straal, CL_P,
                         'no_shadow')
    cross_c_3 = Cylinder([x_pos, y_pos+6, z_pos], [x_pos, y_pos+7, z_pos], straal, CL_B,
                         'no_shadow')
    cross_c_4 = Cylinder([x_pos+22, y_pos+6, z_pos], [x_pos+22, y_pos+7, z_pos], straal, CL_P,
                         'no_shadow')
    return cross_c_1, cross_c_2, cross_c_3, cross_c_4


def make_crossing_cytokinesis_2(x_pos, y_pos, z_pos, straal):
    """This is the crossing-over for the cytokinesis part 2"""
    cross_c_2_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos, y_pos+1, z_pos], straal, CL_B,
                           'no_shadow')
    cross_c_2_2 = Cylinder([x_pos+26, y_pos, z_pos], [x_pos+26, y_pos+1, z_pos], straal, CL_P,
                           'no_shadow')
    cross_c_2_3 = Cylinder([x_pos, y_pos+6, z_pos], [x_pos, y_pos+7, z_pos], straal, CL_B,
                           'no_shadow')
    cross_c_2_4 = Cylinder([x_pos+26, y_pos+6, z_pos], [x_pos+26, y_pos+7, z_pos], straal, CL_P,
                           'no_shadow')
    return cross_c_2_1, cross_c_2_2, cross_c_2_3, cross_c_2_4


def make_spindle_interphase(x_pos, y_pos, z_pos):
    """These are the spindles for interphase"""
    spindle_i_l = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_i_r = Box([x_pos+1, y_pos, z_pos], [x_pos+1.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    return spindle_i_l, spindle_i_r


def make_spindle_interphase_2(x_pos, y_pos, z_pos):
    """These are the spindles for interphase part 2"""
    spindle_i_l = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_i_r = Box([x_pos+3, y_pos-3, z_pos], [x_pos+4.5, y_pos-3.5, z_pos], CL_R, 'no_shadow')
    return spindle_i_l, spindle_i_r


def make_spindle(x_pos, y_pos, z_pos):
    """These are the spindles for prophase"""
    spindle_l = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_r = Box([x_pos+5.5, y_pos-7, z_pos], [x_pos+7, y_pos-7.5, z_pos], CL_R, 'no_shadow')
    return spindle_l, spindle_r


def make_spindle_prophase(x_pos, y_pos, z_pos):
    """These are the spindles for prophase"""
    spindle_p_l = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_p_r = Box([x_pos+13.5, y_pos-2, z_pos], [x_pos+14, y_pos-3.5, z_pos], CL_R, 'no_shadow')
    return spindle_p_l, spindle_p_r


def make_spindle_prophase_2(x_pos, y_pos, z_pos):
    """These are the spindles for prophase"""
    spindle_p_2_l = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_p_2_r = Box([x_pos+13.5, y_pos, z_pos], [x_pos+14, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    return spindle_p_2_l, spindle_p_2_r


def make_spindle_telophase(x_pos, y_pos, z_pos):
    """These are the spindles for telophase"""
    spindle_t_l = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_t_r = Box([x_pos+18, y_pos, z_pos], [x_pos+18.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    return spindle_t_l, spindle_t_r


def make_spindle_telophase_3(x_pos, y_pos, z_pos):
    """These are the spindles for telophase"""
    spindle_t_3_l = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_t_3_r = Box([x_pos+24, y_pos, z_pos], [x_pos+24.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    return spindle_t_3_l, spindle_t_3_r


def make_spindle_c(x_pos, y_pos, z_pos):
    """These are the spindles for cytokinesis"""
    spindle_c_1 = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_c_2 = Box([x_pos+23.5, y_pos, z_pos], [x_pos+24, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    return spindle_c_1, spindle_c_2


def make_spindle_c_2(x_pos, y_pos, z_pos):
    """These are the spindles for cytokinesis"""
    spindle_c_2_1 = Box([x_pos, y_pos, z_pos], [x_pos+0.5, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    spindle_c_2_2 = Box([x_pos+21.5, y_pos, z_pos], [x_pos+22, y_pos+1.5, z_pos], CL_R, 'no_shadow')
    return spindle_c_2_1, spindle_c_2_2


def make_fiber_l(x_pos, y_pos, z_pos, straal):
    """These are the fibers left for interphase and prophase"""
    f_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos+3, z_pos], straal, CL_R, 'no_shadow')
    f_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos+1, z_pos], straal, CL_R, 'no_shadow')
    f_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos-1, z_pos], straal, CL_R, 'no_shadow')
    f_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos-3, z_pos], straal, CL_R, 'no_shadow')
    return f_1, f_2, f_3, f_4


def make_fiber_r(x_pos, y_pos, z_pos, straal):
    """These are the fibers right for interphase and prophase"""
    f_r_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos-3, y_pos+2, z_pos], straal, CL_R, 'no_shadow')
    f_r_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos-1, y_pos+2, z_pos], straal, CL_R, 'no_shadow')
    f_r_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+1, y_pos+2, z_pos], straal, CL_R, 'no_shadow')
    f_r_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+3, y_pos+2, z_pos], straal, CL_R, 'no_shadow')
    return f_r_1, f_r_2, f_r_3, f_r_4


def make_fiber_p_c_l(x_pos, y_pos, z_pos, straal):
    """This is the fibers left for prophase crossing-over"""
    f_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos+3, z_pos], straal, CL_R, 'no_shadow')
    f_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos+1, z_pos], straal, CL_R, 'no_shadow')
    f_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos-1, z_pos], straal, CL_R, 'no_shadow')
    f_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos-3, z_pos], straal, CL_R, 'no_shadow')
    return f_1, f_2, f_3, f_4


def make_fiber_p_c_r(x_pos, y_pos, z_pos, straal):
    """These are the fibers right for prophase crossing-over"""
    f_2_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos-2, y_pos+3, z_pos], straal, CL_R, 'no_shadow')
    f_2_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos-2, y_pos+1, z_pos], straal, CL_R, 'no_shadow')
    f_2_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos-2, y_pos-1, z_pos], straal, CL_R, 'no_shadow')
    f_2_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos-2, y_pos-3, z_pos], straal, CL_R, 'no_shadow')
    return f_2_1, f_2_2, f_2_3, f_2_4


def make_fiber_m_l(x_pos, y_pos, z_pos, straal):
    """These are the fibers left for metaphase"""
    f_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+7, y_pos+4.5, z_pos+2], straal, CL_R, 'no_shadow')
    f_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos+7, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+7, y_pos-2, z_pos+2], straal, CL_R, 'no_shadow')
    f_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+7, y_pos-4, z_pos-1], straal, CL_R, 'no_shadow')
    return f_1, f_2, f_3, f_4


def make_fiber_m_r(x_pos, y_pos, z_pos, straal):
    """These are the fibers right for metaphase"""
    f_2_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos-7, y_pos+4.5, z_pos+2], straal, CL_R,
                     'no_shadow')
    f_2_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos-7, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_2_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos-7, y_pos-2, z_pos+2], straal, CL_R, 'no_shadow')
    f_2_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos-7, y_pos-4, z_pos-1], straal, CL_R, 'no_shadow')
    return f_2_1, f_2_2, f_2_3, f_2_4


def make_fiber_t_l(x_pos, y_pos, z_pos, straal):
    """These are the fibers left for telophase"""
    f_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+9.3, y_pos+4, z_pos+3], straal, CL_R, 'no_shadow')
    f_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+9.3, y_pos-2, z_pos+3], straal, CL_R, 'no_shadow')
    f_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos-3.5, z_pos-1], straal, CL_R,
                   'no_shadow')
    return f_1, f_2, f_3, f_4


def make_fiber_a_l(x_pos, y_pos, z_pos, straal):
    """These are the fibers left for anaphase"""
    f_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+7, y_pos+4, z_pos+2], straal, CL_R, 'no_shadow')
    f_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+7, y_pos-2, z_pos+2], straal, CL_R, 'no_shadow')
    f_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos-3.5, z_pos-1], straal, CL_R,
                   'no_shadow')
    return f_1, f_2, f_3, f_4


def make_fiber_a_r(x_pos, y_pos, z_pos, straal):
    """These are the fibers right for anaphase"""
    f_2_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos-7, y_pos+4, z_pos+2], straal, CL_R, 'no_shadow')
    f_2_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_2_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos-7, y_pos-2, z_pos+2], straal, CL_R, 'no_shadow')
    f_2_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos-3.5, z_pos-1], straal, CL_R,
                     'no_shadow')
    return f_2_1, f_2_2, f_2_3, f_2_4


def make_fiber_t_r(x_pos, y_pos, z_pos, straal):
    """These are the fibers right for telophase"""
    f_2_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos-9.3, y_pos+4, z_pos+3], straal, CL_R,
                     'no_shadow')
    f_2_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_2_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos-9.3, y_pos-2, z_pos+3], straal, CL_R,
                     'no_shadow')
    f_2_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos-3.5, z_pos-1], straal, CL_R,
                     'no_shadow')
    return f_2_1, f_2_2, f_2_3, f_2_4


def make_fiber_t_2_l(x_pos, y_pos, z_pos, straal):
    """These are the fibers left for telophase part 2"""
    f_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+8, y_pos+4, z_pos+3], straal, CL_R, 'no_shadow')
    f_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+8, y_pos-2, z_pos+3], straal, CL_R, 'no_shadow')
    f_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos-3.5, z_pos-1], straal, CL_R,
                   'no_shadow')
    return f_1, f_2, f_3, f_4


def make_fiber_t_2_r(x_pos, y_pos, z_pos, straal):
    """These are the fibers right for telophase part 2"""
    f_2_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos-8, y_pos+4, z_pos+3], straal, CL_R, 'no_shadow')
    f_2_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_2_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos-8, y_pos-2, z_pos+3], straal, CL_R, 'no_shadow')
    f_2_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos-3.5, z_pos-1], straal, CL_R,
                     'no_shadow')
    return f_2_1, f_2_2, f_2_3, f_2_4


def make_fiber_t_3_l(x_pos, y_pos, z_pos, straal):
    """These are the fibers left for telophase part 3 and cytokinesis"""
    f_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4, y_pos+4, z_pos+3], straal, CL_R, 'no_shadow')
    f_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4, y_pos-2, z_pos+3], straal, CL_R, 'no_shadow')
    f_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+4.5, y_pos-3.5, z_pos-1], straal, CL_R,
                   'no_shadow')
    return f_1, f_2, f_3, f_4


def make_fiber_t_3_r(x_pos, y_pos, z_pos, straal):
    """These are the fibers right for telophase part 3 and cytokinesis"""
    f_2_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos+4, z_pos+3], straal, CL_R, 'no_shadow')
    f_2_2 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos+2, z_pos-1], straal, CL_R, 'no_shadow')
    f_2_3 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos-2, z_pos+3], straal, CL_R, 'no_shadow')
    f_2_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos-4, y_pos-3.5, z_pos-1], straal, CL_R,
                     'no_shadow')
    return f_2_1, f_2_2, f_2_3, f_2_4


def make_chromatide(x_pos, y_pos, z_pos, straal):
    """These are the chromatides for interphase"""
    cylinder_1 = Cylinder([x_pos, y_pos, z_pos], [x_pos+1.5, y_pos, z_pos], straal, CL_B,
                          'no_shadow')
    cylinder_2 = Cylinder([x_pos, y_pos-1, z_pos], [x_pos+1, y_pos+1, z_pos+1], straal, CL_P,
                          'no_shadow')
    cylinder_3 = Cylinder([x_pos, y_pos+1, z_pos], [x_pos+2, y_pos+2, z_pos], straal, CL_B,
                          'no_shadow')
    cylinder_4 = Cylinder([x_pos, y_pos, z_pos], [x_pos+2, y_pos+1, z_pos+1], straal, CL_P,
                          'no_shadow')
    return cylinder_1, cylinder_2, cylinder_3, cylinder_4


def split_cel(x_pos, y_pos, z_pos):
    """These are the cells that grow apart in telophase part 1"""
    cel_1 = Sphere([-2, 3, 4], 8, CL_BASE, 'translate', [x_pos, y_pos, z_pos+4], 'no_shadow')
    cel_2 = Sphere([2, 3, 4], 8, CL_BASE, 'translate', [x_pos, y_pos, z_pos+4], 'no_shadow')
    return cel_1, cel_2


def split_cel_t(x_pos, y_pos, z_pos):
    """These are the cells that grow apart in telophase part 2"""
    cel_t_1 = Sphere([-2, 3, 4], 7, CL_BASE, 'translate', [x_pos-4, y_pos, z_pos+4], 'no_shadow')
    cel_t_2 = Sphere([2, 3, 4], 7, CL_BASE, 'translate', [x_pos+3, y_pos, z_pos+4], 'no_shadow')
    return cel_t_1, cel_t_2


def split_cel_t_3(x_pos, y_pos, z_pos):
    """These are the cells that grow apart in telophase part 3"""
    cel_t_1 = Sphere([-2, 3, 4], 6.5, CL_BASE, 'translate', [x_pos-5, y_pos, z_pos+4], 'no_shadow')
    cel_t_2 = Sphere([2, 3, 4], 6.5, CL_BASE, 'translate', [x_pos+3, y_pos, z_pos+4], 'no_shadow')
    return cel_t_1, cel_t_2


def split_cel_c(x_pos, y_pos, z_pos):
    """These are the cells that grow apart in cytokinesis part 2"""
    cel_c_1 = Sphere([-2, 3, 4], 6.3, CL_BASE, 'translate', [x_pos-6, y_pos, z_pos+4], 'no_shadow')
    cel_c_2 = Sphere([2, 3, 4], 6.3, CL_BASE, 'translate', [x_pos+4, y_pos, z_pos+4], 'no_shadow')
    return cel_c_1, cel_c_2


def split_cel_c_2(x_pos, y_pos, z_pos):
    """These are the cells that grow apart in cytokinesis part 4"""
    cel_c_1 = Sphere([-2, 3, 4], 6.3, CL_BASE_1, 'translate', [x_pos-6, y_pos, z_pos+4],
                     'no_shadow')
    cel_c_2 = Sphere([2, 3, 4], 6.3, CL_BASE_1, 'translate', [x_pos+4, y_pos, z_pos+4], 'no_shadow')
    return cel_c_1, cel_c_2


def split_cel_c_3(x_pos, y_pos, z_pos):
    """These are the cells that grow apart in cytokinesis part 3"""
    cel_c_1 = Sphere([-2, 3, 4], 6.3, CL_BASE, 'translate', [x_pos-5, y_pos, z_pos+4],
                     'no_shadow')
    cel_c_2 = Sphere([2, 3, 4], 6.3, CL_BASE, 'translate', [x_pos+3, y_pos, z_pos+4], 'no_shadow')
    return cel_c_1, cel_c_2


def new_nuc(x_pos, y_pos, z_pos):
    """These are for the new nucleus in cytokinesis part 1,2,3"""
    nuc_l = Sphere([-1, 5, 0], 2.5, CL_NUC, 'translate', [x_pos-4, y_pos, z_pos], 'no_shadow')
    nuc_r = Sphere([-1, 5, 0], 2.5, CL_NUC, 'translate', [x_pos+4, y_pos, z_pos], 'no_shadow')
    return nuc_l, nuc_r


def interphase():
    """This is everything for interphase"""
    spindles = make_spindle_interphase(-4, 4, 0)
    spindles_2 = make_spindle_interphase_2(-4, 4, 0)
    meiose_base = make_meiose_base(0, 5, 0, 5)
    chromatides = make_chromatide(1, 4.5, 0, 0.02)
    inter = make_meiose_trans()
    fibers_l = make_fiber_l(-4, 4.75, 0, 0.01)
    fibers_r = make_fiber_r(-0.25, 0.5, 0, 0.01)
    chromosoom_1 = make_chromosome_b(3.5, -5, 65, 0.3)
    chromosoom_2 = make_chromosome_b(8.5, -5, 65, 0.3)
    chromosoom_3 = make_chromosome_p(3.5, 1, 65, 0.3)
    chromosoom_4 = make_chromosome_p(8.5, 1, 65, 0.3)
    return spindles, spindles_2, inter, chromatides, meiose_base, fibers_l, fibers_r, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4


def prophase_1():
    """This is everything for prophase part 1"""
    zoomed_base = zoom_nuc_base_in(1, 0, -12.5)
    chromosoom_1 = make_chromosome_b(1, 0.5, -5, 0.3)
    chromosoom_2 = make_chromosome_b(-3, 0.5, -5, 0.3)
    chromosoom_3 = make_chromosome_p(1, 6.5, -5, 0.3)
    chromosoom_4 = make_chromosome_p(-3, 6.5, -5, 0.3)
    spindles = make_spindle(-8, 3, -5)
    fibers_l = make_fiber_l(-8, 3.75, -5, 0.01)
    fibers_r = make_fiber_r(-1.75, -4.5, -5, 0.01)
    return zoomed_base, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4, spindles, fibers_l, fibers_r


def prophase_2():
    """This is everything for prophase part 2"""
    zoomed_base = zoom_nuc_base_in(1, 0, -12.5)
    spindles = make_spindle(-8, 3, -5)
    chromosome_1 = make_chromosome_b(1.7, 4, -4, 0.3)
    chromosome_2 = make_chromosome_b(-2.5, 4, -4, 0.3)
    chromosome_3 = make_chromosome_p(1, 4, -5, 0.3)
    chromosome_4 = make_chromosome_p(-3, 4, -5, 0.3)
    fibers_l_2 = make_fiber_l(-8, 3.75, -5, 0.01)
    fibers_r_2 = make_fiber_r(-1.75, -4.5, -5, 0.01)
    return zoomed_base, spindles, chromosome_1, chromosome_2, chromosome_3, chromosome_4, fibers_l_2, fibers_r_2


def prophase_crossing_over():
    """This is everything for prophase the crossing-over"""
    crossing_chromosoom_1 = make_crossing_chromosome_b(1.7, 4, -4, 0.3)
    crossing_chromosoom_2 = make_crossing_chromosome_b(-2.5, 4, -4, 0.3)
    crossing_chromosoom_3 = make_crossing_chromosome_p(1, 4, -5, 0.3)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-3, 4, -5, 0.3)
    crossing_over = make_crossing_prophase(-3, 1, -5, 0.3)
    z_base = zoom_base_in(1, 0, -12.5)
    spindles_prophase = make_spindle_prophase(-8, 3, -5)
    spindles_prophase_2 = make_spindle_prophase_2(-8, 3, -5)
    fibers_p_l = make_fiber_p_c_l(-8, 3.75, -5, 0.01)
    fibers_p_r = make_fiber_p_c_r(6, 0.25, -5, 0.01)
    fibers_p_2_r = make_fiber_p_c_r(6, 3.75, -5, 0.01)
    return crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over, z_base, spindles_prophase, spindles_prophase_2, fibers_p_l, fibers_p_r, fibers_p_2_r


def metaphase():
    """This is everything for metaphase"""
    crossing_chromosoom_1 = make_crossing_chromosome_b(-1.5, 6, -4, 0.3)
    crossing_chromosoom_2 = make_crossing_chromosome_b(-1.5, 0, -4, 0.3)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-2, 6, -5, 0.3)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-2, 0, -5, 0.3)
    crossing_over_m = make_crossing_metaphase(-2, -3, -5, 0.3)
    z_base = zoom_base_in(1, 0, -12.5)
    spindles_prophase_2 = make_spindle_prophase_2(-8, 3, -5)
    fibers_m_l = make_fiber_m_l(-8, 3.75, -5, 0.01)
    fibers_m_r = make_fiber_m_r(6, 3.75, -5, 0.01)
    return crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_m, z_base, spindles_prophase_2, fibers_m_l, fibers_m_r


def anaphase():
    """This is everything for anaphase"""
    crossing_chromosoom_1 = make_crossing_chromosome_b(1, 6, -4, 0.3)
    crossing_chromosoom_2 = make_crossing_chromosome_b(1, 0, -4, 0.3)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-5, 6, -4, 0.3)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-5, 0, -4, 0.3)
    crossing_over_a = make_crossing_anaphase(-5, -3, -4, 0.3)
    z_base = zoom_base_in(1, 0, -12.5)
    spindles_prophase_2 = make_spindle_prophase_2(-8, 3, -5)
    fibers_a_l = make_fiber_a_l(-8, 3.75, -5, 0.01)
    fibers_a_r = make_fiber_a_r(6, 3.75, -5, 0.01)
    return crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_a, z_base, spindles_prophase_2, fibers_a_l, fibers_a_r


def telophase_1():
    """This is everything for telophase part 1"""
    cells = split_cel(1, 0, -12.5)
    crossing_chromosoom_1 = make_crossing_chromosome_b(6, 6, -4, 0.3)
    crossing_chromosoom_2 = make_crossing_chromosome_b(6, 0, -4, 0.3)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-5, 6, -4, 0.3)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-5, 0, -4, 0.3)
    crossing_over_t = make_crossing_telophase(-5, -3, -4, 0.3)
    spindles_t = make_spindle_telophase(-8, 3, -5)
    fibers_t_l = make_fiber_t_l(-8, 3.75, -5, 0.01)
    fibers_t_r = make_fiber_t_r(10.5, 3.75, -5, 0.01)
    return cells, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_t, spindles_t, fibers_t_l, fibers_t_r


def telophase_2():
    """This is everything for telophase part 2"""
    cells = split_cel_t(1, 1, -12.5)
    crossing_chromosoom_1 = make_crossing_chromosome_b(6, 7, -4, 0.3)
    crossing_chromosoom_2 = make_crossing_chromosome_p(6, 1, -4, 0.3)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-5, 7, -4, 0.3)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-5, 1, -4, 0.3)
    crossing_over_t = make_crossing_telophase(-5, -2, -4, 0.3)
    spindles_t_2 = make_spindle_telophase(-8, 4, -5)
    fibers_t_2_l = make_fiber_t_2_l(-8, 4.75, -5, 0.01)
    fibers_t_2_r = make_fiber_t_2_r(10.5, 4.75, -5, 0.01)
    return cells, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_t, spindles_t_2, fibers_t_2_l, fibers_t_2_r


def telophase_3():
    """This is everything for telophase part 3"""
    cells_t = split_cel_t_3(1, 1, -12.5)
    crossing_chromosoom_1 = make_crossing_chromosome_b(8, 7, -4, 0.3)
    crossing_chromosoom_2 = make_crossing_chromosome_b(8, 1, -4, 0.3)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-9, 7, -4, 0.3)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-9, 1, -4, 0.3)
    crossing_over_t_3 = make_crossing_telophase_3(-9, -2, -4, 0.3)
    spindles_t_3 = make_spindle_telophase_3(-12, 4, -5)
    fibers_t_3_l = make_fiber_t_3_l(-12, 4.75, -5, 0.01)
    fibers_t_3_r = make_fiber_t_3_r(12.5, 4.75, -5, 0.01)
    return cells_t, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_t_3, spindles_t_3, fibers_t_3_l, fibers_t_3_r


def cytokinesis_1():
    """This is everything for cytokinesis part 1"""
    cells_c = split_cel_t_3(1, 0, -12.5)
    crossing_chromosoom_1 = make_crossing_chromosome_b(10, 3, 12, 0.3)
    crossing_chromosoom_2 = make_crossing_chromosome_b(10, -3, 12, 0.3)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-12, 3, 12, 0.3)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-12, -3, 12, 0.3)
    crossing_over_c = make_crossing_cytokinesis(-12, -6, 12, 0.3)
    spindles_c = make_spindle_c(-12, 3, -5)
    nucs = new_nuc(1, 0, -12.5)
    fibers_c_l = make_fiber_t_3_l(-12, 3.75, -5, 0.01)
    fibers_c_r = make_fiber_t_3_r(12, 3.75, -5, 0.01)
    return cells_c, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c, spindles_c, nucs, fibers_c_l, fibers_c_r


def cytokinesis_2():
    """This is everything for cytokinesis part 2"""
    cells_c_2 = split_cel_t_3(1, 0, -12.5)
    crossing_chromosoom_1 = make_crossing_chromosome_b(10, 3, 12, 0.03)
    crossing_chromosoom_2 = make_crossing_chromosome_b(10, -3, 12, 0.03)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-12, 3, 12, 0.03)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-12, -3, 12, 0.03)
    crossing_over_c_2 = make_crossing_cytokinesis(-12, -6, 12, 0.03)
    spindles_c_2 = make_spindle_c(-12, 3, -5)
    nucs = new_nuc(1, 0, -12.5)
    fibers_c_l = make_fiber_t_3_l(-12, 3.75, -5, 0.01)
    fibers_c_r = make_fiber_t_3_r(12, 3.75, -5, 0.01)
    return cells_c_2, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c_2, spindles_c_2, nucs, fibers_c_l, fibers_c_r


def cytokinesis_3():
    """This is everything for cytokinesis part 3 and 4"""
    cells_c_3 = split_cel_c(1, 0, -12.5)
    crossing_chromosoom_1 = make_crossing_chromosome_b(12, 3, 12, 0.03)
    crossing_chromosoom_2 = make_crossing_chromosome_b(12, -3, 12, 0.03)
    crossing_chromosoom_3 = make_crossing_chromosome_p(-14, 3, 12, 0.03)
    crossing_chromosoom_4 = make_crossing_chromosome_p(-14, -3, 12, 0.03)
    crossing_over_c_3 = make_crossing_cytokinesis_2(-14, -6, 12, 0.03)
    spindles_c_4 = make_spindle_c_2(-11, 3, -5)
    new_nucs = new_nuc(1, 0, -12.5)
    new_base = split_cel_c_2(1, 0, -12.5)
    new_cells = split_cel_c_3(1, 0, -12.5)
    return cells_c_3, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c_3, spindles_c_4, new_nucs, new_base, new_cells


def frame(step):
    """This describes what happens at every step returns it"""
    meiose = Text('ttf', '"timrom.ttf"', '"Meiose 1"', 0, 0, 'scale', 1,
                  Texture(Pigment('color', [1, 1, 1]), Finish('phong', 0.6, 'reflection', 0.6)),
                  'translate', [-2, 5, -15])

    interphase_text = Text('ttf', '"cyrvetic.ttf"', '"Interphase 1"', 0, 0, 'scale', 1,
                           Texture(Pigment('color', [1, 1, 1]), Finish('phong', 0.6,
                                                                       'reflection', 0.6)),
                           'translate', [8, 10, 0])

    prophase_text = Text('ttf', '"cyrvetic.ttf"', '"Prophase 1"', 0, 0, 'scale', 1,
                         Texture(Pigment('color', [1, 1, 1]), Finish('phong', 0.6,
                                                                     'reflection', 0.6)),
                         'translate', [8, 10, 0])

    metaphase_text = Text('ttf', '"cyrvetic.ttf"', '"Metaphase 1"', 0, 0, 'scale', 1,
                          Texture(Pigment('color', [1, 1, 1]), Finish('phong', 0.6,
                                                                      'reflection', 0.6)),
                          'translate', [8, 10, 0])


    anaphase_text = Text('ttf', '"cyrvetic.ttf"', '"Anaphase 1"', 0, 0, 'scale', 1,
                         Texture(Pigment('color', [1, 1, 1]), Finish('phong', 0.6,
                                                                     'reflection', 0.6)),
                         'translate', [8, 10, 0])

    telophase_text = Text('ttf', '"cyrvetic.ttf"', '"Telophase 1"', 0, 0, 'scale', 1,
                          Texture(Pigment('color', [1, 1, 1]), Finish('phong', 0.6,
                                                                      'reflection', 0.6)),
                          'translate', [8, 10, 0])

    cytokinesis_text = Text('ttf', '"cyrvetic.ttf"', '"Cytokinesis 1"', 0, 0, 'scale', 1,
                            Texture(Pigment('color', [1, 1, 1]), Finish('phong', 0.6,
                                                                        'reflection', 0.6)),
                            'translate', [8, 10, 0])
    light = LightSource([2, 8, -20], 1)
    if step >= 0 <= 40:
        objects = [light, Union(Intersection(meiose))]
    if step >= 41 <= 80:
        objects = [light, Union(Intersection(interphase_text))]
        spindles, spindles_2, inter, chromatides, meiose_base, fibers_l, fibers_r, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4 = interphase()
        objects += meiose_base
    if step >= 81 <= 120:
        objects = [light, Union(Intersection(interphase_text))]
        spindles, spindles_2, inter, chromatides, meiose_base, fibers_l, fibers_r, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4 = interphase()
        objects += inter
    if step >= 121 <= 160:
        objects = [light, Union(Intersection(interphase_text))]
        spindles, spindles_2, inter, chromatides, meiose_base, fibers_l, fibers_r, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4 = interphase()
        objects += spindles
        objects += inter
    if step >= 161 <= 200:
        objects = [light, Union(Intersection(interphase_text))]
        spindles, spindles_2, inter, chromatides, meiose_base, fibers_l, fibers_r, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4 = interphase()
        objects += spindles
        objects += chromatides
        objects += inter
    if step >= 201 <= 240:
        objects = [light, Union(Intersection(interphase_text))]
        spindles, spindles_2, inter, chromatides, meiose_base, fibers_l, fibers_r, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4 = interphase()
        objects += spindles_2
        objects += chromatides
        objects += inter
        objects += fibers_l
        objects += fibers_r
    if step >= 241 <= 280:
        objects = [light, Union(Intersection(interphase_text))]
        spindles, spindles_2, inter, chromatides, meiose_base, fibers_l, fibers_r, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4 = interphase()
        objects += spindles_2
        objects += inter
        objects += fibers_l
        objects += fibers_r
        objects += chromosoom_1
        objects += chromosoom_2
        objects += chromosoom_3
        objects += chromosoom_4
    if step >= 281 <= 320:
        objects = [light, Union(Intersection(prophase_text))]
        zoomed_base, chromosoom_1, chromosoom_2, chromosoom_3, chromosoom_4, spindles, fibers_l, fibers_r = prophase_1()
        objects += chromosoom_1
        objects += chromosoom_2
        objects += chromosoom_3
        objects += chromosoom_4
        objects += spindles
        objects += zoomed_base
        objects += fibers_l
        objects += fibers_r
    if step >= 321 <= 360:
        objects = [light, Union(Intersection(prophase_text))]
        zoomed_base, spindles, chromosome_1, chromosome_2, chromosome_3, chromosome_4, fibers_l_2, fibers_r_2 = prophase_2()
        objects += chromosome_1
        objects += chromosome_2
        objects += chromosome_3
        objects += chromosome_4
        objects += zoomed_base
        objects += spindles
        objects += fibers_l_2
        objects += fibers_r_2
    if step >= 361 <= 400:
        objects = [light, Union(Intersection(prophase_text))]
        zoomed_base, spindles, chromosome_1, chromosome_2, chromosome_3, chromosome_4, fibers_l_2, fibers_r_2 = prophase_2()
        crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over, z_base, spindles_prophase, spindles_prophase_2, fibers_p_l, fibers_p_r, fibers_p_2_r = prophase_crossing_over()
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over
        objects += zoomed_base
        objects += spindles
        objects += fibers_l_2
        objects += fibers_r_2
    if step >= 401 <= 440:
        objects = [light, Union(Intersection(prophase_text))]
        crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over, z_base, spindles_prophase, spindles_prophase_2, fibers_p_l, fibers_p_r, fibers_p_2_r = prophase_crossing_over()
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over
        objects += z_base
        objects += spindles_prophase
        objects += fibers_p_l
        objects += fibers_p_r
    if step >= 441 <= 480:
        objects = [light, Union(Intersection(prophase_text))]
        crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over, z_base, spindles_prophase, spindles_prophase_2, fibers_p_l, fibers_p_r, fibers_p_2_r = prophase_crossing_over()
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over
        objects += spindles_prophase_2
        objects += z_base
        objects += fibers_p_l
        objects += fibers_p_2_r
    if step >= 481 <= 520:
        objects = [light, Union(Intersection(metaphase_text))]
        crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_m, z_base, spindles_prophase_2, fibers_m_l, fibers_m_r = metaphase()
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_m
        objects += z_base
        objects += spindles_prophase_2
        objects += fibers_m_l
        objects += fibers_m_r
    if step >= 521 <= 560:
        objects = [light, Union(Intersection(anaphase_text))]
        crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_a, z_base, spindles_prophase_2, fibers_a_l, fibers_a_r = anaphase()
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_a
        objects += z_base
        objects += spindles_prophase_2
        objects += fibers_a_l
        objects += fibers_a_r
    if step >= 561 <= 600:
        objects = [light, Union(Intersection(telophase_text))]
        cells, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_t, spindles_t, fibers_t_l, fibers_t_r = telophase_1()
        objects += cells
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_t
        objects += spindles_t
        objects += fibers_t_l
        objects += fibers_t_r
    if step >= 601 <= 640:
        objects = [light, Union(Intersection(telophase_text))]
        cells, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_t, spindles_t_2, fibers_t_2_l, fibers_t_2_r = telophase_2()
        objects += cells
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_t
        objects += spindles_t_2
        objects += fibers_t_2_l
        objects += fibers_t_2_r
    if step >= 641 <= 680:
        objects = [light, Union(Intersection(telophase_text))]
        cells_t, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_t_3, spindles_t_3, fibers_t_3_l, fibers_t_3_r = telophase_3()
        objects += cells_t
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_t_3
        objects += spindles_t_3
        objects += fibers_t_3_l
        objects += fibers_t_3_r
    if step >= 681 <= 720:
        objects = [light, Union(Intersection(cytokinesis_text))]
        cells_c, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c, spindles_c, nucs, fibers_c_l, fibers_c_r = cytokinesis_1()
        objects += cells_c
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_c
        objects += spindles_c
        objects += fibers_c_l
        objects += fibers_c_r
        objects += nucs
    if step >= 721 <= 760:
        objects = [light, Union(Intersection(cytokinesis_text))]
        cells_c, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c, spindles_c, nucs, fibers_c_l, fibers_c_r = cytokinesis_1()
        objects += cells_c
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_c
        objects += spindles_c
        objects += nucs
        objects += fibers_c_l
        objects += fibers_c_r
    if step >= 761 <= 800:
        objects = [light, Union(Intersection(cytokinesis_text))]
        cells_c_2, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c_2, spindles_c_2, nucs, fibers_c_l, fibers_c_r = cytokinesis_2()
        objects += cells_c_2
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_c_2
        objects += spindles_c_2
        objects += nucs
        objects += fibers_c_l
        objects += fibers_c_r
    if step >= 801 <= 840:
        objects = [light, Union(Intersection(cytokinesis_text))]
        cells_c_3, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c_3, spindles_c_4, new_nucs, new_base, new_cells = cytokinesis_3()
        objects += new_cells
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_c_3
        objects += spindles_c_4
        objects += new_nucs
    if step >= 841 <= 880:
        objects = [light, Union(Intersection(cytokinesis_text))]
        cells_c_3, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c_3, spindles_c_4, new_nucs, new_base, new_cells = cytokinesis_3()
        objects += cells_c_3
        objects += crossing_chromosoom_1
        objects += crossing_chromosoom_2
        objects += crossing_chromosoom_3
        objects += crossing_chromosoom_4
        objects += crossing_over_c_3
        objects += spindles_c_4
        objects += new_nucs
    if step >= 881 <= 920:
        objects = [light, Union(Intersection(cytokinesis_text))]
        cells_c_3, crossing_chromosoom_1, crossing_chromosoom_2, crossing_chromosoom_3, crossing_chromosoom_4, crossing_over_c_3, spindles_c_4, new_nucs, new_base, new_cells = cytokinesis_3()
        objects += new_base
    return Scene(models.default_camera, objects)


if __name__ == '__main__':
    pypovray.render_scene_to_mp4(frame)

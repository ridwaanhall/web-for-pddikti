from flask import jsonify, request
from urllib.parse import quote
from app.Controller import MahasiswaController, PerguruanTinggiController, ProdiController, DosenController, HitController
from app import app

@app.route('/')
def index():
    return 'hello Flask'

@app.route('/hit_mhs/<string:mahasiswa>', methods=['GET'])
def hit_mhs_route(mahasiswa):
    # Encode the mahasiswa parameter to handle special characters
    encoded_mahasiswa = quote(mahasiswa)
    
    # Use the encoded_mahasiswa as input for the MahasiswaController.hit_mhs() function
    data = MahasiswaController.hit_mhs(encoded_mahasiswa)
    return jsonify(data)

@app.route('/data_mahasiswa/<string:link_mhs>', methods=['GET'])
def data_mahasiswa(link_mhs):
    data = MahasiswaController.data_mahasiswa(link_mhs)
    return jsonify(data)

@app.route('/load_pt', methods=['GET'])
def load_pt():
    data = PerguruanTinggiController.load_pt()
    return jsonify(data)

@app.route('/data_pt/<string:link_pt>', methods=['GET'])
def data_pt(link_pt):
    data = PerguruanTinggiController.data_pt(link_pt)
    return jsonify(data)

@app.route('/data_pt_prodi/<string:link_pt>', methods=['GET'])
def data_pt_prodi(link_pt):
    data = PerguruanTinggiController.data_pt_prodi(link_pt)
    return jsonify(data)

@app.route('/data_pt_jumlah/<string:link_pt>', methods=['GET'])
def data_pt_jumlah(link_pt):
    data = PerguruanTinggiController.data_pt_jumlah(link_pt)
    return jsonify(data)

@app.route('/data_pt_dosen/<string:link_pt>', methods=['GET'])
def data_pt_dosen(link_pt):
    data = PerguruanTinggiController.data_pt_dosen(link_pt)
    return jsonify(data)

@app.route('/stat_pt/<string:link_pt>', methods=['GET'])
def stat_pt(link_pt):
    data = PerguruanTinggiController.stat_pt(link_pt)
    return jsonify(data)

@app.route('/load_prodi', methods=['GET'])
def load_prodi():
    data = ProdiController.load_prodi()
    return jsonify(data)

@app.route('/load_prodi/<string:id_sp>', methods=['GET'])
def load_detail_prodi(id_sp):
    data = ProdiController.load_detail_prodi(id_sp)
    return jsonify(data)

@app.route('/data_prodi/<string:link_prodi>', methods=['GET'])
def data_prodi(link_prodi):
    data = ProdiController.data_prodi(link_prodi)
    return jsonify(data)

@app.route('/data_dosen/<string:link_dosen>', methods=['GET'])
def data_dosen(link_dosen):
    data = DosenController.data_dosen(link_dosen)
    return jsonify(data)

@app.route('/hit/<string:dsn_prodi_pt>', methods=['GET'])
def hit_dsn_prodi_pt_route(dsn_prodi_pt):
    # Encode the dsn_prodi_pt parameter to handle special characters
    encoded_dsn_prodi_pt = quote(dsn_prodi_pt)
    
    # Use the encoded_dsn_prodi_pt as input for the dsn_prodi_ptController.hit_mhs() function
    data = HitController.hit(encoded_dsn_prodi_pt)
    return jsonify(data)
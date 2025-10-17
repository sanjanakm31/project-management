import React, { useEffect, useState } from 'react';
import API from '../api';

export default function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [me, setMe] = useState(null);
  const token = localStorage.getItem('access');

  useEffect(() => {
    if (!token) return;
    API.get('projects/', { headers: { Authorization: `Bearer ${token}` } })
      .then(r => setProjects(r.data))
      .catch(() => {});
    // get user info from token payload (quick decode)
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      setMe(payload);
    } catch (e) {}
  }, []);

  const save = async (p) => {
    const token = localStorage.getItem('access');
    await API.put(`projects/${p.id}/`, p, {
      headers: { Authorization: `Bearer ${token}` },
    });
    const res = await API.get('projects/', {
      headers: { Authorization: `Bearer ${token}` },
    });
    setProjects(res.data);
  };

  const exportCSV = () =>
    window.open('http://localhost:8000/api/projects/export_csv/');

  return (
    <div style={{ padding: 20 }}>
      <h2>Dashboard {me && me.username}</h2>
      <button onClick={exportCSV}>Export CSV (Admin only)</button>
      <table border="1" cellPadding="6" style={{ marginTop: 20 }}>
        <thead>
          <tr>
            <th>Employee</th>
            <th>Project</th>
            <th>Customer</th>
            <th>Priority</th>
            <th>Due</th>
            <th>Completion</th>
            <th>Delay</th>
            <th>Remarks</th>
            <th>Delay Remarks</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {projects.map((p) => (
            <tr key={p.id}>
              <td>{p.employee.username}</td>
              <td>{p.project_name}</td>
              <td>{p.customer}</td>
              <td>{p.priority}</td>
              <td>{p.due_date}</td>
              <td>
                <input
                  type="number"
                  value={p.completion}
                  onChange={(e) => {
                    p.completion = Number(e.target.value);
                    setProjects([...projects]);
                  }}
                />
              </td>
              <td>{p.delay}</td>
              <td>
                <input
                  value={p.remarks}
                  onChange={(e) => {
                    p.remarks = e.target.value;
                    setProjects([...projects]);
                  }}
                />
              </td>
              <td>
                <input
                  placeholder="Reason for delay"
                  value={p.delay_remarks || ''}
                  onChange={(e) => {
                    p.delay_remarks = e.target.value;
                    setProjects([...projects]);
                  }}
                />
              </td>
              <td>
                <button onClick={() => save(p)}>Save</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}


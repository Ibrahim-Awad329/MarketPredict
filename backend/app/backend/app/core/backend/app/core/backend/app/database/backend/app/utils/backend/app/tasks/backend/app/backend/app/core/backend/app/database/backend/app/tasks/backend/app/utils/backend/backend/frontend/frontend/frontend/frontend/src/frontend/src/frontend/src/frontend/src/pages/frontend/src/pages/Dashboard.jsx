import { Link } from 'react-router-dom'

function Dashboard() {
  return (
    <div className="p-8">
      <h1 className="text-4xl font-bold mb-8">لوحة التحكم</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-800 p-6 rounded-lg">
          <h2 className="text-2xl font-semibold mb-2">الدورات</h2>
          <p className="text-slate-400">0 دورة نشطة</p>
        </div>
        
        <div className="bg-slate-800 p-6 rounded-lg">
          <h2 className="text-2xl font-semibold mb-2">التقدم</h2>
          <p className="text-slate-400">0%</p>
        </div>
        
        <div className="bg-slate-800 p-6 rounded-lg">
          <h2 className="text-2xl font-semibold mb-2">النقاط</h2>
          <p className="text-slate-400">0 نقطة</p>
        </div>
      </div>
      
      <Link to="/" className="inline-block mt-8 text-purple-400 hover:underline">
        الرجوع للرئيسية
      </Link>
    </div>
  )
}

export default Dashboard

// types/classroom.ts
export interface Student {
  id: number
  name: string
  avatar?: string
  position: { x: number; y: number; z: number }
  hasVisionIssue: boolean
  difficultyLearning: boolean
  learningStyle: 'visual' | 'auditory' | 'kinesthetic'
  grades: {
    human: number
    lang: number
    exact: number
    physical: number
    arts: number
  }
  strengths: string[]
  attendance?: AttendanceRecord[]
  notes?: string[]
  dotsProfileId?: number
  groupId?: number
}

export interface AttendanceRecord {
  date: string
  status: 'present' | 'absent' | 'late' | 'excused'
  reason?: string
}

export interface Group {
  id: number
  name: string
  color?: string
  students: number[]
  focus?: string
  createdAt?: Date
}

export interface Classroom {
  id: number
  name: string
  subject: string
  teacher: string
  students: Student[]
  groups: Group[]
  layout3D?: string
  lastUpdated: Date
  schedule?: ClassroomSchedule[]
  resources?: string[]
}

export interface ClassroomSchedule {
  day: string
  startTime: string
  endTime: string
  room: string
}